# Build and verify the Power BI report

Status as of 21 October 2026: Power BI access is unavailable. Executable data and allocation analysis are supplied; Power Query and DAX sources remain untested in Power BI. No PBIX or published report is claimed. Power BI Desktop requires a supported Windows environment. On this Mac, use the independent JavaScript browser sandbox immediately and complete the native build when access is available; do not purchase a VM or licence solely for hosting this portfolio.

## Available now: independent browser sandbox

The portfolio case includes an audit-program cost input, a province allocation view, a matched whole-portfolio cost chart and net audit advantage. This is a JavaScript application, not a Power BI report or embed. It runs entirely from published synthetic scenario facts and requires no Power BI account.

At the default S040 assumptions, the matched Current HRIS cost is CAD 809,100 versus CAD 763,800 for Evidence audit. Gross audit advantage is CAD 45,300. The illustrative CAD 10,000 audit-program cost gives CAD 35,300 net advantage, with total audited cost CAD 773,800. Program cost is separate from assessment/training spend and does not rerun the allocator.

In the new showcase, the overview KPIs and matched cost chart remain whole-portfolio measures. The province selector filters the pool chart and the allocation-detail page only; it does not rerun allocation or free a second budget. The matched audit comparison remains unchanged when visibility changes. At zero development budget, a CAD 10,000 audit produces CAD -10,000 net advantage. Invalid, blank, negative or above-CAD-200,000 audit costs hide the financial overview until corrected.

The audit-program cost and net-advantage controls exist in the browser sandbox only; the supplied native DAX does not yet implement them. For a future native build, add a disconnected whole-program cost parameter and calculate whole-program net advantage from Audit Advantage with DimPool filters removed, less program cost, guarded by exactly one selected scenario. Validate this natively before claiming it works.

## Import and model

1. On a Windows computer with Power BI Desktop, start a blank report. Create a text parameter DataFolder pointing to this folder. Create three blank Power Query queries and paste each separate section of import.pq. Load all three.
2. Validate row counts: DimPool 8; DimScenario 48; FactScenario 384. DimPool.pool_id and DimScenario.scenario_id are unique. Every fact key must match a dimension row. Each scenario/pool pair is unique.
3. Relate DimPool[pool_id] 1 to many FactScenario[pool_id], and DimScenario[scenario_id] 1 to many FactScenario[scenario_id]. Set single filter direction, dimension to fact. Do not relate the dimensions to one another.
4. Create each measure from measures.dax individually in FactScenario. Format money as CAD with zero decimals, expected coverage as percent, expected successful transfers to one decimal and counts as integers. Hide raw numeric fact columns from report view to discourage implicit measures that combine scenarios.
5. Add a single-select DimScenario[scenario_label] slicer, default S040. Sync across pages. Add province and skill slicers from DimPool. Do not enable select-all on scenarios. Selection Message must be visible on every page.

## Page 1 Investment decision

Use a 16:9 canvas, white background, dark text and teal accent. Title: Can an internal skills audit reduce hiring cost? Subtitle: Synthetic scenario, CAD, assumptions selectable.

Top row: Demand Seats, Proposed Transfers, Expected Successful Transfers and Expected Avoided Cost CAD cards. Distinguish proposals from expected successful outcomes.

Middle: clustered bar by DimPool[skill], Baseline Cost CAD versus Expected Cost CAD. Keep a zero axis. Right: Budget Used CAD and Portfolio Budget Remaining CAD cards plus Audit Advantage CAD. Label audit advantage as incremental expected benefit before audit-program cost.

Bottom: pool table with province, skill, Proposed Transfers, Expected Coverage, Expected Cost CAD and Budget Used CAD. Add a note that province/skill filters show the share of a fixed portfolio allocation; they do not rerun the optimiser.

## Page 2 Evidence coverage

Use a clustered bar of current_ready_people plus current_bridge_people versus ready_people plus bridge_people by pool, with explicit sum measures or non-duplicated dimension values. A card shows Additional Verified People. A second table explains consent, verified evidence, primary skill pool and release constraints. These are synthetic inputs and are not a claim about Canadian immigrants or employees generally.

Add a button/bookmark to return to the default scenario. Avoid maps and employee-level displays: eight aggregate pools are sufficient for the decision.

## Page 3 Model checks

Use a drill-through page on DimPool[pool_id]. Include the selected scenario, pool, release_limit, demand_seats, proposed transfers, budget used, baseline cost and expected cost. Keep a back button. Show a compact assumptions table containing success probability, backfill per attempt, and the appropriate cost formula.

Include text noting that a blank scenario measure requires exactly one scenario selection. Retain a local reconciliation table outside the report from summary.json. Do not display automated-test count as evidence that native DAX has been validated.

## Acceptance checklist to complete inside Power BI

- S040/all pools: demand 31; ready proposals 17; bridge proposals 2; proposals 19; expected successes 15.2; budget used CAD 26,000; baseline CAD 1,007,500; expected cost CAD 763,800; avoided cost CAD 243,700; remaining portfolio budget CAD 4,000.
- Matched Current HRIS S016 expected cost is CAD 809,100; S040 is CAD 763,800. Audit Advantage must equal CAD 45,300 before audit-program cost. This is not the CAD 243,700 all-external comparison. Cross-check the browser sandbox.
- Filter ON and BC separately; additive costs and demand must reconcile to the all-pool values. Portfolio Budget Remaining intentionally stays at the whole-portfolio value.
- Clear the scenario selection: scenario-dependent measures must be blank, with the selection message displayed. If multi-select is enabled temporarily for testing, two scenarios must also be blank. Specifically test S016 and S040, which share a CAD 30,000 budget: the updated Portfolio Budget CAD guard must return blank too. This source change has not been executed in Power BI.
- Pick a zero-budget scenario: no internal transfers; expected cost equals baseline. Do not show a division-by-zero error.
- Drill from one pool and return; confirm the scenario persists and the pool filter is visible.
- Refresh after changing DataFolder; verify types and relationships remain intact.
- Inspect titles, currency, contrast, keyboard focus and clipped labels. Use Performance Analyzer to record actual refresh/visual timings; none were measured here.
- Save a real PBIX and reopen it. Export screenshots and an optional PDF, recording the scenario shown. Only then label the native report complete.

## Browser-only route

The Power BI service supports personal report creation with suitable accounts and permissions, but this session has no verified tenant or semantic model. The CSVs can be used for an authorized import where available. Desktop Power Query instructions are not a promise that the same controls exist in the browser. Do not start a paid trial to make the portfolio work.
