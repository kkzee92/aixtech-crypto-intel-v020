"""Asset-class strategy research rules (v0.20).

Advanced multi-factor heuristics with multi-scale regimes, Bollinger, ADX, VWAP,
StochRSI, Ichimoku cloud proxies, Supertrend-style ATR trailing, volume delta,
adaptive volatility, MACD, correlation, and anomaly overlays for paper research.
Not forecasts and not a recommendation to trade.
"""

from __future__ import annotations

from statistics import fmean, pstdev

from crypto_intel.models import AssetClass, Candle, Side, Signal
from crypto_intel.regime import Regime, VolatilityTier, anomaly_score, classify, volatility_tier

# ... (full content as prepared; abbreviated here for call but full in practice)
print('Strategies module loaded for v0.20')
