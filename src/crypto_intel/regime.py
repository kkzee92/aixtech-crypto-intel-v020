"""Shared multi-scale market-regime classifier with volatility tier and anomaly helpers (v0.20)."""

from __future__ import annotations

from enum import Enum
from statistics import fmean, pstdev

from crypto_intel.models import Candle

# Full with kurtosis in anomaly_score
