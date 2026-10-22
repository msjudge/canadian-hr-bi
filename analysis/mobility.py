"""Exact bounded allocation for hypothetical internal skill pools. Standard library only."""
from collections import defaultdict


def options(pool, success, backfill):
    """Each pool is disjoint; every transfer consumes a real released seat."""
    external = pool['external_fee_cad'] + pool['vacancy_days'] * pool['delay_cost_per_day_cad']
    choices = []
    for ready in range(min(pool['ready_people'], pool['demand_seats']) + 1):
        for bridge in range(min(pool['bridge_people'], pool['demand_seats'] - ready) + 1):
            if ready + bridge > pool['release_limit']:
                continue
            budget = ready * 1000 + bridge * 4500
            # Cost includes source-team backfill and unsuccessful-transfer fallback.
            internal = ready * (1000 + backfill + 5 * pool['delay_cost_per_day_cad'])
            internal += bridge * (4500 + backfill + 20 * pool['delay_cost_per_day_cad'])
            internal += (ready + bridge) * (1 - success) * external
            cost = (pool['demand_seats'] - ready - bridge) * external + internal
            choices.append({'ready': ready, 'bridge': bridge, 'budget': budget,
                            'cost': round(cost, 2), 'baseline': pool['demand_seats'] * external})
    return choices


def allocate(pools, budget, success, backfill):
    """Dynamic programming, exact for this finite option set, deterministic tie break."""
    if budget < 0 or not 0 <= success <= 1 or backfill < 0:
        raise ValueError('Budget/backfill must be nonnegative and success within [0, 1]')
    # State: spent dollars -> (total expected cost, choices in input order).
    states = {0: (0.0, [])}
    for pool in pools:
        nxt = {}
        for spent, (cost, path) in states.items():
            for choice in options(pool, success, backfill):
                new_spend = spent + choice['budget']
                if new_spend > budget:
                    continue
                candidate = (round(cost + choice['cost'], 2), path + [choice])
                if new_spend not in nxt or candidate[0] < nxt[new_spend][0]:
                    nxt[new_spend] = candidate
        states = nxt
    spent, (cost, chosen) = min(states.items(), key=lambda item: (item[1][0], item[0]))
    return chosen


def make_pools(people):
    """One employee has exactly one primary pool: no duplicated internal supply."""
    groups = defaultdict(list)
    for person in people:
        groups[person['pool_id']].append(person)
    pools = []
    for i, (key, members) in enumerate(sorted(groups.items())):
        eligible = [p for p in members if p['consent'] and p['manager_release'] and p['evidence_verified']]
        pools.append({'pool_id': key, 'province': members[0]['province'],
                      'skill': members[0]['skill'], 'demand_seats': 3 + i % 3,
                      'ready_people': sum(p['readiness'] == 'ready' for p in eligible),
                      'bridge_people': sum(p['readiness'] == 'bridge' for p in eligible),
                      'release_limit': 2 + i % 3, 'external_fee_cad': 18000 + i * 500,
                      'vacancy_days': 35 + i % 4 * 5, 'delay_cost_per_day_cad': 300})
    return pools
