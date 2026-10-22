# Build Before You Buy: The Business Case for Internal Mobility — LinkedIn launch kit

Publishing note: these URLs are planned destinations, not verified live sites. Publish the matching repository first, open its Pages URL, then copy only the post below. Do not present the browser replicas as native vendor execution.

## Separate post

Before approving another external hire, I wanted to test a different workforce-planning question: could better evidence of internal capability change the investment decision?

I built a synthetic Ontario/B.C. scenario model with 240 employee profiles, eight skill pools and 31 demand seats. The allocation respects employee consent, manager release limits and a shared development budget. It prices backfill, transition delay and the possibility that an internal transfer fails.

Across 48 executed scenarios, the dashboard compares current HRIS visibility with an evidence audit under matched assumptions.

In the default scenario, 19 proposed transfers consume CAD 26,000 of development budget. The audit creates CAD 45,300 of modeled gross advantage over current HRIS visibility, or CAD 35,300 after a CAD 10,000 audit cost. Raise that cost to CAD 50,000 and the advantage becomes negative.

That break-even point is the business case: skills discovery has to earn its own cost.

The showcase includes an allocation ledger, scenario controls, semantic model and DAX/M source. The interactive interface is independently built in the browser, inspired by Power BI. Python produced the scenario facts; native Power BI execution remains pending. All data and financial assumptions are synthetic.

Explore: https://msjudge.github.io/canadian-hr-bi/

#StrategicWorkforcePlanning #PeopleAnalytics #InternalMobility #HRIS

## Project entry

**Title:** Build Before You Buy: The Business Case for Internal Mobility

**Association:** Independent research / personal project. Do not attach it to a real employer.

**Description:** I developed this independent study. Independent scenario study of internal mobility as a workforce investment decision. Modelled 48 budget, visibility, transfer-success and backfill combinations across eight skill pools. Built an interactive BI-style dashboard, allocation ledger and scenario-safe semantic model specification. Default net modeled audit advantage is CAD 35,300; no realized employer savings are claimed. Native Power BI M/DAX sources are included but unexecuted.

**Skills:** Workforce planning · Scenario analysis · Semantic modelling · Skills intelligence · Cost modelling

**Planned URL:** https://msjudge.github.io/canadian-hr-bi/

## Screenshot sequence and captions

### 01 / Price the skills audit against a matched alternative

File: `docs/screenshots/01-overview.png`

Scenario S040 compares the evidence audit with current HRIS visibility at the same budget, success probability and backfill cost. CAD 35,300 is a modeled net advantage after the default audit cost; the all-external benchmark answers a different question.

### 02 / Follow the decision to the pool ledger

File: `docs/screenshots/02-allocation.png`

Demand, manager release capacity, ready transfers and development-bridge transfers are visible together. The default allocation proposes 17 ready and two bridge moves. Expected successes are probability-weighted proposals, not observed transfers.

### 03 / Protect the scenario grain

File: `docs/screenshots/03-model.png`

DimPool and DimScenario relate to FactScenario at one pool by one complete scenario. Adding mutually exclusive scenarios would duplicate demand. The dashboard selects one scenario; the supplied DAX uses single-scenario guards for a future native implementation.

## Posting sequence

Use this project as its own post and project entry. Attach the overview first, then the technical evidence; keep the caption text adjacent to each image where the interface allows it. Add the verified live dashboard to Featured as a separate work sample. The report can be attached as a document when you want a longer methods walkthrough. Review the draft in your own voice before posting.
