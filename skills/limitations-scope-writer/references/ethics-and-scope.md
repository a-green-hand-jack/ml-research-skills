# Ethics, Broader Impact, and Deployment Scope

Use this reference when a venue or paper topic requires social, ethical, safety, privacy, or deployment caveats.

## Ethics Paragraph Jobs

Common jobs:

- identify data or annotation risks
- identify misuse or dual-use risk
- identify fairness, bias, or representation limits
- identify privacy or consent constraints
- identify deployment preconditions
- state release restrictions or safeguards

Do not claim mitigations that are not implemented or planned.

## Broader Impact Scope

A useful broader-impact paragraph should distinguish:

- what the paper enables
- who may benefit
- who may be harmed
- what assumptions are required for responsible use
- what the authors do or do not release

Avoid generic statements that could apply to any ML paper.

## Deployment Caveats

Use deployment caveats when:

- experiments are offline but the paper implies real-world use
- the method depends on curated data
- human oversight is required
- errors have high cost
- robustness or safety was not fully evaluated

Suggested moves:

1. State that evaluation is limited to the studied setting.
2. Name the missing deployment evidence.
3. State what should be checked before deployment.

## Data and Privacy Caveats

Mention:

- data source and consent limitations
- personally identifiable information risks
- domain representation limits
- annotation or labeling assumptions
- restrictions on redistribution

## Misuse Caveats

Use when the method could enable harmful generation, surveillance, manipulation, security attacks, or automated decision-making.

Moves:

1. State the misuse channel.
2. State whether the artifact release changes the risk.
3. State any concrete safeguards or limitations.
4. Avoid pretending the risk is solved if it is only acknowledged.

## Claim Downgrade Examples

- "deployable" -> "evaluated in offline settings"
- "safe" -> "does not address all safety risks"
- "fair" -> "evaluated on the measured group metrics"
- "privacy-preserving" -> "reduces exposure under the tested threat model"
- "human-level" -> "matches or exceeds human performance on this benchmark"
