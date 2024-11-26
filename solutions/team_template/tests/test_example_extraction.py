"""
Example test implementation showing expected structure and patterns.
Use this as a reference for their own test implementations.
"""

import pytest
from unittest.mock import patch
from team_template.src.extraction import EPDExtractor

def test_example_extraction_complete():
    """Fully implemented example test with detailed comments."""
    extractor = EPDExtractor()
    
    # Test data setup
    test_data = {
        "impact_categories": [
            {
                "name": "Global Warming Potential",
                "value": 12.3,
                "unit": "kg CO2 eq."
            }
        ]
    }
    
    # Validation test
    is_valid, issues = extractor.validate_extraction(test_data)
    
    # Assertions with explanatory comments
    assert isinstance(is_valid, bool), "Validation should return boolean"
    assert isinstance(issues, list), "Issues should be returned as list"
    assert is_valid, f"Valid data should pass validation. Issues: {issues}"
