# EPL ML Research

Historical research archive for English Premier League match prediction and betting experiments.

## Scope

- Understat match data: EPL 2015-08-08 through 2024-05-19
- Football-Data opening B365 odds: 2022/23 and 2023/24 for the locked comparison
- V7: walk-forward probabilistic model
- V10: value-bet selection experiment
- V11-A: linear shrinkage toward the market
- V11-C: divergence-band dynamic shrinkage
- Development period: 2022/23
- Final locked OOS period: 2023/24
- Market baseline: B365 opening 1X2 odds converted to fair probabilities

## Final OOS conclusion

The market baseline was the strongest model on the main probabilistic metrics in the locked 2023/24 OOS period.

| Model | LogLoss | Brier | Accuracy |
|---|---:|---:|---:|
| Market | **0.91074** | **0.17807** | **59.63%** |
| V11-A | 0.91602 | 0.17905 | 58.05% |
| V11-C | 0.91655 | 0.17907 | 58.84% |
| V7 | 0.96278 | 0.18961 | 55.15% |

Betting experiments also failed OOS:

- V10: **-24.12% ROI**, 266 final bets
- V11-A: **-65.87% ROI**, 52 final bets

These results are treated as an experimental conclusion, not as evidence that markets are universally efficient.

## Methodological principles

1. Keep match-time information out of pre-match features.
2. Use chronological walk-forward validation.
3. Separate development decisions from the final OOS period.
4. Lock parameters before evaluating final OOS.
5. Use the bookmaker market as a serious baseline.
6. Do not equate LogLoss improvement with betting ROI.
7. Do not re-optimize a failed final OOS result.
8. Report negative results honestly.

## Important data note

2024/25 is not included in the final Understat-based model comparison because the corresponding Understat model data was not available in this experiment. It should be treated as a separate future protocol, not silently mixed into this one.

## Status

**Research line frozen.**

The correct conclusion is:

> Modeli marketi yenene kadar zorlamak yerine, marketi yenemediğimizi OOS testleriyle kanıtlayıp araştırmayı durdurduk.
