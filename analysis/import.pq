// Create a TEXT parameter named DataFolder, ending without a slash.
// Set it to the local analysis folder. Create three separate queries below.

// Query name: DimPool
let
    Source = Csv.Document(File.Contents(DataFolder & "/DimPool.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {
        {"pool_id", type text}, {"province", type text}, {"skill", type text},
        {"demand_seats", Int64.Type}, {"ready_people", Int64.Type},
        {"bridge_people", Int64.Type}, {"release_limit", Int64.Type},
        {"external_fee_cad", Currency.Type}, {"vacancy_days", Int64.Type},
        {"delay_cost_per_day_cad", Currency.Type},
        {"current_ready_people", Int64.Type}, {"current_bridge_people", Int64.Type}
    }, "en-CA")
in Types

// Query name: DimScenario
let
    Source = Csv.Document(File.Contents(DataFolder & "/DimScenario.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {
        {"scenario_id", type text}, {"visibility", type text},
        {"budget_cad", Currency.Type}, {"success_probability", type number},
        {"backfill_per_transfer_cad", Currency.Type}, {"scenario_label", type text}
    }, "en-CA")
in Types

// Query name: FactScenario
let
    Source = Csv.Document(File.Contents(DataFolder & "/FactScenario.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {
        {"scenario_id", type text}, {"pool_id", type text},
        {"demand_seats", Int64.Type}, {"ready_transfers", Int64.Type},
        {"bridge_transfers", Int64.Type}, {"budget_used_cad", Currency.Type},
        {"expected_successful_transfers", type number},
        {"baseline_cost_cad", Currency.Type}, {"expected_cost_cad", Currency.Type},
        {"expected_cost_avoided_cad", Currency.Type}
    }, "en-CA")
in Types
