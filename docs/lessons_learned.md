# Lessons Learned

1. Walk-forward validation is necessary for this temporal problem.
2. Development performance is not evidence of OOS performance.
3. A market baseline is mandatory for model evaluation.
4. Better LogLoss does not guarantee profitable betting.
5. Grid search can overfit; V11-C improved development but failed final OOS.
6. Strong positive model-vs-market divergence was a recurring warning region.
7. Small betting samples are noisy; the 41-bet development result is not evidence of durability.
8. Do not re-optimize after seeing the final OOS result.
9. 2024/25 requires a separate protocol because the required Understat model data was unavailable.
10. Negative results are useful and should be preserved.

## Final principle

Modeli marketi yenene kadar zorlamak yerine, marketi yenemediğimizi OOS testleriyle kanıtlayıp araştırmayı durdurduk.
