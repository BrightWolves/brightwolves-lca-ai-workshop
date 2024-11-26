"""Shared pytest fixtures and configuration."""

import pytest
from pathlib import Path

@pytest.fixture(scope="session")
def test_data_dir():
    """Get path to test data directory."""
    return Path(__file__).parent / "data"

# solutions/team_template/tests/helpers/mock_data.py
"""Mock data utilities for testing."""

from dataclasses import dataclass
from typing import Dict, List, Any
import pandas as pd

@dataclass
class MockEPD:
    """Mock EPD data structure for testing."""
    text: str
    tables: List[Dict[str, Any]]
    expected_outputs: Dict[str, float]

SAMPLE_EPD = MockEPD(
    text="Sample EPD content",
    tables=[{
        "impact_category": ["GWP", "AP"],
        "value": [12.3, 0.08],
        "unit": ["kg CO2 eq.", "kg SO2 eq."]
    }],
    expected_outputs={
        "gwp": 12.3,
        "acidification": 0.08
    }
)