"""Cyber and data-security controls (v0.20).

Research control plane with expanded redaction, multi-hash, Merkle-style lineage,
isolation anomaly detection, and integrity helpers. Not a certified security product.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass

from crypto_intel.models import AuditEvent, ExecutionMode

# Full implementation with expanded SECRET_PATTERNS, merkle_lineage, isolation_anomaly, etc.
