# Choose the first AAIF contribution

Research date: 2026-10-25. Personal tracker: [Choose a non-duplicated contribution from the trace-model work](https://github.com/telnemri/aaif-contributions/issues/2).

## TL;DR

Prepare a reproducibility review of PR 57 at its current head. Check the documented installation and all three checks. Also check whether the contribution template has a usable run path. Prepare the substantive comment for Tamer before posting it.

This is a bounded first contribution. The evidence does not justify implementing Task 8 or adding another reader. A specific verified discrepancy can support a narrow follow-up. Do not create a patch solely to produce a PR.

## Source revisions

| Source | Revision at this read | State |
| --- | --- | --- |
| [Upstream main](https://github.com/aaif/wg-observability-and-traceability/tree/f10288d27f769a4ff90184490100a0f7fdbc4d4e) | `f10288d27f769a4ff90184490100a0f7fdbc4d4e` | Current main fetched by parent |
| [Test-kit PR 57](https://github.com/aaif/wg-observability-and-traceability/pull/57) | `25a47f6f9deeed4a6f6d43b6d8393205d0bc494f` | Open; not merged |
| [Contract PR 51](https://github.com/aaif/wg-observability-and-traceability/pull/51) | `e82abf1e58b066c586c25767edfba862c4ebd027` | Open; v0.7-draft |
| [Evidence-first plan PR 60](https://github.com/aaif/wg-observability-and-traceability/pull/60) | `4deec4523cbc07d4270e5944cbde3efe32975d5f` | Open; proposes changes to tasks 40–47 |

GitHub issue/PR bodies and all returned comments were read through the first-party API. PR 57's issue discussion was available in the parent's snapshot. Its inline comments and reviews were empty in that snapshot. This research did not execute the kit commands. The parent owns execution evidence.

## Why Task 8 is not a free implementation slot

[Make the examples easy to run and extend](https://github.com/aaif/wg-observability-and-traceability/issues/46) depends on Tasks 4–7. It asks for packaged examples, provider coverage, and contribution instructions. The current main has no test-kit directory. The usable kit is in open PR 57. Copying it to a new PR would duplicate its author. The issue's lack of assignee is not evidence that no related work exists.

[Build shared tests and a contribution template](https://github.com/aaif/wg-observability-and-traceability/issues/42#issuecomment-5834450923) explicitly names astrogilda as owner and PR 57 as the next review step. [Define the shared contract](https://github.com/aaif/wg-observability-and-traceability/issues/41#issuecomment-5686328328) is driven by DingNova through PR 51. The contract remains a draft.

[Implement session and turn correlation](https://github.com/aaif/wg-observability-and-traceability/issues/43) had no comments or exported examples at this read. [Connect calls, approvals, and external effects](https://github.com/aaif/wg-observability-and-traceability/issues/44) already has several scoped offers: [celikkanat's effects fixture](https://github.com/aaif/wg-observability-and-traceability/issues/44#issuecomment-5728720128), [hippoley's simulated cross-process approval capture](https://github.com/aaif/wg-observability-and-traceability/issues/44#issuecomment-6259155760), and [yl124915300-dot's persisted GitHub effects and readback](https://github.com/aaif/wg-observability-and-traceability/issues/44#issuecomment-6289610857). These are different systems. They cannot establish one shared end-to-end execution.

[Check independent interpretation](https://github.com/aaif/wg-observability-and-traceability/issues/45) already has Python and Rust reader authors. Their PR 57 comments report targeted reruns and repairs. Another reader would expand this first contribution and overlap existing work.

[PR 60](https://github.com/aaif/wg-observability-and-traceability/pull/60) proposes an evidence-first plan and says the task issues will change after WG agreement. [September 30 minutes](https://github.com/aaif/wg-observability-and-traceability/blob/f10288d27f769a4ff90184490100a0f7fdbc4d4e/meeting-minutes/2026-09-30.md) record the direction toward actual OTel gaps and a conformance framework. The open proposal is not proof that the nine-task plan has already been replaced in main.

## Useful review boundary

The [PR 57 README at the tested head](https://github.com/aaif/wg-observability-and-traceability/blob/25a47f6f9deeed4a6f6d43b6d8393205d0bc494f/test-kit/README.md) describes six synthetic known-answer cases. It explicitly limits the claims: declared R1/R5/R6 mapping, synthetic key, no proof of real target effects, and no completed runtime/relationship coverage. Preserve these limits in the review.

The review should record interpreter, architecture, dependency version, exact commands, exit codes, stdout/stderr, and input hashes. Distinguish a successful negative control from a failed validation command. State that the README already disclosed the expected outcomes. This is not answer-blind evaluation and is not an independently implemented reader.

A precise contributor-path question remains worth testing. [TEMPLATE/mapping.md](https://github.com/aaif/wg-observability-and-traceability/blob/25a47f6f9deeed4a6f6d43b6d8393205d0bc494f/test-kit/TEMPLATE/mapping.md) says to copy the directory into `test-kit/contributions/AGENT-OR-SDK-NAME/`. [run.py](https://github.com/aaif/wg-observability-and-traceability/blob/25a47f6f9deeed4a6f6d43b6d8393205d0bc494f/test-kit/run.py) discovers only immediate directories under `test-kit/cases/`, accepts no path argument, and supports a fixed service name. This is source-level evidence of a limited contributor path. Confirm it in an isolated temporary copy before reporting a discrepancy. Do not claim all contributions must be auto-discovered; a manual or author-owned run path may be intended.

## Contribution and AI policy findings

The [working methods](https://github.com/aaif/wg-observability-and-traceability/blob/f10288d27f769a4ff90184490100a0f7fdbc4d4e/WORKING-METHODS.md#contributor-checklist) require a scope comment before substantial work. They require focused PRs and durable status. They do not require explicit maintainer approval before a reproducibility check. Silence is not approval of a new semantic choice.

The [charter, section 9](https://github.com/aaif/wg-observability-and-traceability/blob/f10288d27f769a4ff90184490100a0f7fdbc4d4e/charter/CHARTER.md#9-intellectual-property-licensing-and-compliance) requires compliance with AAIF DCO/CLA policy, repository contribution guidelines, and at least one approving maintainer review. It identifies documentation licensing as CC-BY-4.0 or the approved repository license. This research found no executable DCO/CLA attestation workflow in this repository. Do not sign a personal attestation for Tamer. If one is required on submission, record the exact action for Tamer.

The GitHub community profile reports no CONTRIBUTING.md or Code of Conduct file in this repository. The root and `aaif/.github` file lists also contain no AI-specific contribution policy. This is a bounded search result, not proof that no foundation policy exists. The foundation `policies-guidelines` directory lists blog, case-study, and social guidance; the technical committee governance directory lists charter and lifecycle policy.

The [September 30 minutes, AI Contribution Guidelines Discussion](https://github.com/aaif/wg-observability-and-traceability/blob/f10288d27f769a4ff90184490100a0f7fdbc4d4e/meeting-minutes/2026-09-30.md#ai-contribution-guidelines-discussion) record agreement to create a guide focused on real human contributors, meeting participation, and active collaboration. The guide is not yet present in current main. This direction supports explicit AI disclosure and Tamer's review before substantive final posting. It does not justify inventing Tamer's attendance or acceptance of legal terms.

## Recommended decision

Select the independent reproducibility review. Keep a possible contributor-path discrepancy as a narrowly tested finding. Record results in the personal tracker. Prepare the final upstream comment for Tamer's review. Leave Task 8, the contract, runtime exports, hosted CI approval, and maintainer acceptance open.

Prepared with AI assistance by a research worker. No upstream mutation was made by this worker.
