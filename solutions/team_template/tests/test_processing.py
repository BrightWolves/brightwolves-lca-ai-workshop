# exercises/test_processing.py
"""
Exercise 2: Test LCA Data Processing Functions

Learning Objectives:
1. Test unit conversion logic for common LCA metrics
2. Verify impact category calculations
3. Ensure proper handling of different data quality levels
4. Validate uncertainty propagation in calculations

Tips:
- Use pytest.mark.parametrize for testing multiple unit conversions
- Consider significant figures in environmental impact calculations
- Think about error bounds and uncertainty in LCA data
"""

import pytest
from team_template.src.processing import LCAProcessor
from ..helpers.mock_data import SAMPLE_INVENTORY_DATA

class TestLCAProcessor:
    def test_unit_conversions(self, processor):
        """
        TODO: Test unit conversion functionality
        
        Hints:
        - Test common LCA unit pairs (e.g., kg CO2 eq. -> g CO2 eq.)
        - Consider prefix conversions (micro, milli, kilo)
        - Verify handling of compound units (kg CO2 eq./kWh)
        - Check precision and rounding behavior
        
        Example structure:
        test_cases = [
            (1000, "g CO2 eq.", "kg CO2 eq.", 1.0),
            (0.001, "kg SO2 eq.", "g SO2 eq.", 1.0),
            ...
        ]
        """
        pass  # Your implementation

    def test_impact_calculation(self, processor):
        """
        TODO: Test environmental impact calculations
        
        Hints:
        - Verify GWP (Global Warming Potential) calculations
        - Test multiple impact categories together
        - Check aggregation of different emission sources
        - Validate characterization factors
        
        Focus areas:
        1. Direct emissions
        2. Energy-related impacts
        3. Transport emissions
        4. Process-specific factors
        """
        pass  # Your implementation

    def test_data_quality(self, processor):
        """
        TODO: Test data quality assessment
        
        Hints:
        - Check handling of uncertain data
        - Verify quality indicators
        - Test completeness checks
        - Validate temporal relevance
        
        Quality aspects:
        1. Geographical representation
        2. Temporal correlation
        3. Technological correlation
        4. Reliability
        5. Completeness
        """
        pass  # Your implementation