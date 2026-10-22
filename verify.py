from pathlib import Path
import json,csv,sqlite3,sys
ROOT=Path(__file__).resolve().parent
A=ROOT/'analysis'
def rows(n):
 r=list(csv.DictReader((A/n).open()))
 for x in r:
  for k,v in x.items():
   try:x[k]=float(v) if '.' in v else int(v)
   except(ValueError,TypeError):pass
 return r
sys.path.insert(0,str(A))
from mobility import allocate
pools=rows('DimPool.csv');facts=rows('FactScenario.csv');scenarios=rows('DimScenario.csv')
assert len(scenarios)==48 and len(facts)==384
for s in scenarios:
 p=[dict(x) for x in pools]
 if s['visibility']=='Current HRIS':
  for x in p:x['ready_people']=x['current_ready_people'];x['bridge_people']=x['current_bridge_people']
 choices=allocate(p,s['budget_cad'],s['success_probability'],s['backfill_per_transfer_cad'])
 actual=[f for f in facts if f['scenario_id']==s['scenario_id']]
 assert sum(c['budget'] for c in choices)<=s['budget_cad']
 for pool,c in zip(p,choices):
  f=next(f for f in actual if f['pool_id']==pool['pool_id'])
  assert c['ready']==f['ready_transfers'] and c['bridge']==f['bridge_transfers']
  assert abs(c['cost']-f['expected_cost_cad'])<.01
  assert c['ready']+c['bridge']<=min(pool['demand_seats'],pool['release_limit'])
print('PASS: all 48 scenarios / 384 pool allocations reproduced; demand, release and shared development-budget constraints hold. Native Power BI execution not performed.')
