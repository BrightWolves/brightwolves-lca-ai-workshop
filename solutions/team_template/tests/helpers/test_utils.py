"""Test utility functions."""

from pathlib import Path
from typing import Any, Dict
from unittest.mock import Mock
import pandas as pd
from ...src.extraction import EPDExtractor  # Relative import from tests directory
from ...src.processing import LCAProcessor

def load_test_epd(filepath: Path) -> Dict[str, Any]:
    """Load test EPD data from file."""
    # Implementation for students
    pass

def create_mock_extractor(**kwargs) -> Mock:
    """Create a mock EPDExtractor for testing."""
    mock_extractor = Mock(spec=EPDExtractor)
    # Set up default mock behaviors
    return mock_extractor

def create_mock_processor(**kwargs) -> Mock:
    """Create a mock LCAProcessor for testing."""
    mock_processor = Mock(spec=LCAProcessor)
    # Set up default mock behaviors
    return mock_processor