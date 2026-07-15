# Expected Behavior

## Evaluation contract

Each eval run must record:

- run ID;
- timestamp;
- repository HEAD SHA;
- skill version;
- execution tool and model;
- case ID;
- normalized inputs;
- Scene Specification or stop reason;
- prompt plan when generation is allowed;
- diagnostic codes;
- QA decision;
- output manifest when an asset is produced;
- pass, fail, or blocked result;
- known nondeterminism.

## Pass conditions

A positive case passes only when:

1. the required input is present;
2. every reference has an explicit role, `take`, and `do_not_take` contract;
3. exactly one transformation mode is selected;
4. semantic, identity, composition, and style locks are recorded;
5. the Scene Specification contains exact dimensions, aspect ratio, style ID, and style version;
6. the prompt plan preserves style-pack invariants and excludes prohibited markers;
7. staged flows approve composition and geometry before material and lighting refinement;
8. visual QA is completed;
9. no critical defect remains;
10. the final image is visible to the user and the output manifest confirms delivery.

A negative case passes when the skill stops or corrects at the documented gate and does not silently continue with degraded assumptions.

## Critical regressions

The following results fail the complete eval run regardless of other case scores:

- an unavailable edit target is invented;
- conflicting style references are merged without approval;
- a style ID is used without an exact version;
- an AI-generated Finuslugi logo is accepted;
- a critical defect is accepted because the weighted score is high;
- a local correction regenerates the full scene and breaks approved locks;
- generation succeeds but the final response contains no visible image;
- an output manifest declares `visible_to_user: false` or `response_non_empty: false`.

## Visual comparison

Visual regression is manual until an approved golden set exists. Reviewers must compare:

- communication meaning;
- subject identity and mandatory features;
- object count;
- composition and negative space;
- style-pack invariants;
- material and light behavior;
- brand asset use;
- technical artifacts;
- final delivery.

A golden image may be replaced only through explicit review. The PR must state why the old image is no longer canonical and which style or behavior rule changed.

## Repeatability

For nondeterministic generation cases, run at least three attempts with the same Scene Specification. The skill passes repeatability when:

- all attempts preserve semantic and identity locks;
- at least two attempts satisfy primary style invariants;
- failures receive correct diagnostic codes;
- the selected candidate and rejection reasons are recorded.

## Result statuses

- `pass`: all mandatory assertions are satisfied;
- `fail`: one or more mandatory assertions are violated;
- `blocked`: a required capability, approved asset, or legal approval is unavailable;
- `not-run`: case was intentionally excluded and the reason is recorded.
