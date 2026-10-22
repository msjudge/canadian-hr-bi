# Build Before You Buy: The Business Case for Internal Mobility

**Manvir Singh Judge | HR Operations · HRIS · People Analytics**  
Independent research, developed with AI assistance. All operational records and financial assumptions are synthetic.

[Explore the dashboard](https://msjudge.github.io/canadian-hr-bi/) · [Research report](https://msjudge.github.io/canadian-hr-bi/report.pdf) · [Visual walkthrough](https://msjudge.github.io/canadian-hr-bi/screenshots.html) · [LinkedIn](https://www.linkedin.com/in/msjudge/)

## The HR question

I wanted to test whether better evidence of internal capability could change a workforce investment decision. I built a synthetic Ontario/B.C. scenario model with 240 employee profiles, eight skill pools and 31 demand seats. The allocation respects employee consent, manager release and a shared development budget, while pricing backfill, transition delays and unsuccessful transfers.

## What I found

I evaluated 48 matched scenarios. Under the default assumptions, 19 proposed transfers use CAD 26,000 in development funding. A skills-evidence audit produces CAD 45,300 in modeled gross advantage over current HRIS visibility, or CAD 35,300 after a CAD 10,000 audit cost. At a CAD 50,000 audit cost, that advantage becomes negative.

## My interpretation

My conclusion is conditional: an internal skills audit must earn its own cost. I would validate release capacity, transfer success and source-team disruption before recommending investment. These are scenario outputs, not realized employer savings.

## What I implemented

Python produced the scenario facts. The Power BI-inspired dashboard is an independently built browser replica. M and DAX sources are included for a future native implementation; they have not been executed in Power BI.

The dashboard connects management findings to the detailed ledger or evidence register, source logic and research limitations. Captions explain each screenshot's analytical purpose. The report documents population, metric definitions, verification, limitations and the proposed next decision.

## Reproduce the study

Run `python3 verify.py` from this directory. The `analysis/` folder contains the executed implementation and frozen evidence. Serve `docs/` with a local static server or visit the live dashboard above. No paid hosting, database or API is required.

## Scope and authorship

This is my independent portfolio research, not work attributed to a current or former employer. Browser interfaces are clearly labelled replicas. Consult the report before interpreting any modeled financial or governance outcome.
