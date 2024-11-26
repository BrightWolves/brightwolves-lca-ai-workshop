# helpers/mock_data.py
"""Mock data utilities for testing."""

from dataclasses import dataclass
from typing import Dict, List, Any

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

# helpers/test_utils.py
"""Test utility functions."""

from pathlib import Path
from typing import Any, Dict
import pandas as pd

def load_test_epd(filepath: str) -> Dict[str, Any]:
    """Load test EPD data from file."""
    # Implementation for students
    pass

def create_mock_extractor(**kwargs):
    """Create a mock EPDExtractor for testing."""
    # Implementation for students
    pass

def create_mock_processor(**kwargs):
    """Create a mock LCAProcessor for testing."""
    # Implementation for students
    pass

# helpers/__init__.py
"""Test utilities and shared fixtures."""

from .mock_data import MockEPD, SAMPLE_EPD
from .test_utils import (
    load_test_epd,
    create_mock_extractor,
    create_mock_processor
)

__all__ = [
    'MockEPD',
    'SAMPLE_EPD',
    'load_test_epd',
    'create_mock_extractor',
    'create_mock_processor'
]

# test_processing.py
"""Tests for the LCA processing functionality."""

import pytest
from team_template.src.processing import LCAProcessor

def test_processor_initialization():
    """Test LCAProcessor initialization."""
    processor = LCAProcessor()
    assert hasattr(processor, 'unit_conversions')
    assert hasattr(processor, 'impact_categories')

# Add more test implementations for students