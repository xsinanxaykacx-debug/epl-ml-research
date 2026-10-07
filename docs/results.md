# Results

## Final locked OOS: 2023/24

| Model | LogLoss | Brier | Accuracy |
|---|---:|---:|---:|
| Market | **0.91074** | **0.17807** | **59.63%** |
| V11-A | 0.91602 | 0.17905 | 58.05% |
| V11-C | 0.91655 | 0.17907 | 58.84% |
| V7 | 0.96278 | 0.18961 | 55.15% |

Market wins the three headline metrics in the final OOS comparison.

## Development

V11-A:
- Market LogLoss: 0.96723
- V7 LogLoss: 0.98633
- Best alpha: 0.20
- V11-A LogLoss: 0.96450

V11-C:
- Best configuration: (0.00, 0.40, 0.20)
- LogLoss: 0.96384

The development gains did not survive final OOS.

## Betting

V10:
- Development threshold: 10%
- Development: 275 bets, +12.20% ROI
- Final: 266 bets, -24.12% ROI

V11-A:
- Development: 41 bets, +116.22% ROI
- Final: 52 bets, -65.87% ROI

The development returns are treated as variance/selection warnings, not evidence of a durable strategy.

## Divergence diagnostic

In the final period, strong positive V7-vs-market divergence was associated with materially worse V7 error in the major class-specific subsets. Similar behavior was observed in development.

The archive deliberately avoids calling this proven structural causality.
