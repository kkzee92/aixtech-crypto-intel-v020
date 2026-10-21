# Asset-class strategy notes (v0.20)

These rules are research heuristics. Each class has an edge hypothesis, an
entry, an invalidation, a horizon, and a size cap. They are not a promise of
return. Version 0.20 adds Supertrend proxies, volume-delta filters, and
kurtosis-aware anomaly overlays.

Regime labels, from `regime.py`:

- **trend**: multi-span move of sufficient magnitude and bar range under the stress band
- **range**: neither stress nor trend
- **stress**: average bar range at least 3.5% of price; directional ideas stand aside

## Major

Hypothesis: liquid majors trend with multi-factor confirmation including Supertrend and volume delta, unless RSI/StochRSI is stretched or the book is in stress/high anomaly. Mean reversion is allowed only in a range regime. Cap 8%. Horizon 8 or 20 bars. Research cost 8 bps round trip.

## Large-cap alt

Hypothesis: breakouts without volume, momentum, and positive volume delta are noise, and stress-regime breakouts are gap risk. Entry needs multi-confirmation outside stress. Cap 4%. Cost 14 bps.

## Stablecoin

Hypothesis: the useful signal is a peg break. Adaptive deviation, z-score, consecutive, and skew alerts only. Risk gate forces size to zero. Cost assumption is unused because no order is allowed.

## DeFi

Hypothesis: trend signals in high realised-volatility, stress, or high-anomaly regimes are mostly gap risk. Stand aside if multi-scale conditions fail. Cap 2%. Cost 22 bps.

## Meme

Hypothesis: most bursts are untradeable. A long is allowed only after qualified burst with volume consistency, positive delta, StochRSI not extreme, and extension filter. Horizon is 3 bars. Cap 0.5%. Cost 45 bps.

## L2

Hypothesis: L2 tokens are bets on relative strength versus a benchmark with volume and correlation support. No benchmark, stressed benchmark, or low correlation means no trade. Cap 3%. Cost 16 bps.

## RWA

Hypothesis: tokenised real-world assets should be slow. An open-to-prior-close gap above adaptive threshold, stress, high vol, or high anomaly halts the idea. Cap 2%, horizon 24 bars. Cost 12 bps.

## Perpetual

Hypothesis: negative funding with contained multi-bar drift, stability, consistency, and positive volume delta is a carry observation. Funding at or above 10 bps is a crowded-funding alert, not a short. Cap 2%. Cost 10 bps. This does not model liquidation, funding intervals, or exchange risk.

## Still out of scope

- Live order routing, withdrawal, and trade API keys.
- A broker adapter. That would be a separate human-approved system.
- Claims about future returns. Scores describe the synthetic fixture.
