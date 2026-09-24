# Patent Value Ledgers

Each JSONL row is one patent-value ledger conforming to `schema/patent-value-ledger.schema.json`.

Current status: **1.0 Draft**.

Hard rules:
- Unknown is allowed and preferred over invented precision.
- Product / enterprise value does not automatically become patent value.
- Patent-level R3/R4/R5 requires an exact-patent → value-carrier link.
- R5 requires explicit patent-level attributable value evidence.
- Historical ledgers must respect their T0 cutoff.

The first public example is `example-aikening.jsonl`.
