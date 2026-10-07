# Methodology

## Prediction target

Pre-match 1X2 probabilities: Home, Draw, Away.

## Walk-forward

The original V7 evaluation used chronological walk-forward validation with a verified refit interval of 10 matches.

Original V7 summary:
- 3,397 usable matches
- 2,377 training observations
- 1,020 test observations
- Test dates: 2021-11-21 to 2024-05-19
- Accuracy: 54.90%
- LogLoss: 0.97417
- Brier mean: 0.19252

## Market baseline

Opening B365H/D/A odds were converted to fair probabilities:

q = 1 / odds

p = q / sum(q)

Average bookmaker overround was approximately 5.40%. This is overround, not ROI.

## Development and final OOS

Development: 2022/23.
Final locked OOS: 2023/24.

No final-period parameter re-optimization was permitted.

## V10 betting

Threshold candidates: 0%, 2%, 3%, 4%, 5%, 7%, 10%.
The development-selected threshold was 10% and was locked for final OOS.
Stake was 100 TL.

## V11-A

P11 = alpha * P_V7 + (1-alpha) * P_market

Development selected alpha = 0.20 using LogLoss, then locked it for final OOS.

## V11-C

Dynamic alpha used three maximum-absolute divergence bands:
- <5 percentage points
- 5–10 percentage points
- >=10 percentage points

Development search evaluated 343 combinations and selected:
- <5 pp: 0.00
- 5–10 pp: 0.40
- >=10 pp: 0.20

These values were locked for final OOS.

## Interpretation

A development gain is not evidence of a persistent edge. The locked final OOS result is decisive.
