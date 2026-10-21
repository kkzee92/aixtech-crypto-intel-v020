# AIxTech crypto intel v0.20: enhanced paper-only trading information system

Further advanced research harness for automated cryptocurrency **information** and paper strategy evaluation.
Builds on [kkzee92/aixtech-crypto-intel-v10](https://github.com/kkzee92/aixtech-crypto-intel-v10), prior versions, and the original [zeekiankok92/aixtech-crypto-intel](https://github.com/zeekiankok92/aixtech-crypto-intel).

It does not place live orders, does not store exchange secrets, and is not financial advice.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![version](https://img.shields.io/badge/version-0.20.0-blue)
![mode](https://img.shields.io/badge/execution-paper%20only-orange)
![Licence](https://img.shields.io/badge/licence-MIT-green)

## Enhancements in v0.20

- Supertrend-style ATR trailing proxy and volume-delta confirmation across major classes.
- Kurtosis-enhanced anomaly scoring in regime classification.
- Expanded secret redaction (AWS keys, GitHub PATs, Slack tokens, connection strings).
- Merkle-style lineage root over audit digests and isolation anomaly proxy for zero-trust.
- Adaptive volume-delta filters in breakout, meme, L2, and perpetual rules.
- Updated multi-factor entry conditions with Supertrend and delta gates.

See [docs/asset-class-strategies.md](docs/asset-class-strategies.md) and [docs/security-architecture.md](docs/security-architecture.md).

## What it does

- Eight asset classes with advanced multi-factor research rules incorporating StochRSI, cloud, Supertrend, and volume delta.
- Multi-scale regime + volatility tier + kurtosis-aware anomaly scoring.
- Signals with EMA, MACD, Bollinger, ADX, VWAP, StochRSI, cloud, Supertrend, volume delta, then multi-gate risk.
- Paper-only backtests with class costs; enhanced hash-chained audit + Merkle lineage.
- Synthetic candles only. No network by default.

| Asset class | Enhanced research rule (v0.20) | Risk cap (base) | Cost |
|---|---|---|---|
| Major | Multi-EMA + MACD + Bollinger + ADX + VWAP + StochRSI + cloud + Supertrend + volume delta; stand aside stress/high-vol/anomaly | 8% | 8 bps |
| Large-cap alt | Volume + multi-momentum + MACD + Bollinger + VWAP + StochRSI + volume delta confirmation | 4% | 14 bps |
| Stablecoin | Adaptive peg + multi-stat (z, consecutive, skew) alerts only | 0% | n/a |
| DeFi | Calm multi-scale + channel + momentum + cloud + Supertrend + low anomaly | 2% | 22 bps |
| Meme | Qualified burst with volume profile, delta, StochRSI not extreme, consistency filters | 0.5% | 45 bps |
| L2 | Multi-period RS + relative volume + delta + correlation + consistency vs benchmark | 3% | 16 bps |
| RWA | Slow multi-scale low-vol trend with cloud + Supertrend, adaptive gap, momentum, anomaly | 2% | 12 bps |
| Perpetual | Funding carry with adaptive drift, stability, consistency, non-stress, low anomaly, volume delta | 2% | 10 bps |

## Run

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
python scripts/make_fixtures.py
PYTHONPATH=src python -m crypto_intel scan fixtures/candles_synthetic.json
PYTHONPATH=src python -m crypto_intel brief fixtures/candles_synthetic.json
PYTHONPATH=src python -m crypto_intel posture fixtures/candles_synthetic.json
```

## Controls

Paper-only. No live credentials. Class caps, adaptive confidence and sizing, kill switch, drawdown, statistical anomaly + correlation + StochRSI + Supertrend gates, hash-chained audit, Merkle lineage, expanded redaction, PDPA tripwire, gitleaks. Zero-trust research design.

## Honesty

No live exchange connector. Scores describe synthetic fixtures. Not investment, legal, or compliance advice. Research only.
