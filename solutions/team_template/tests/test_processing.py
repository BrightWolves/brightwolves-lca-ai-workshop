def test_unit_conversion():
    """Test conversion between common units."""
    processor = LCAProcessor()
    result = processor.standardize_units(1000, "g", "kg")
    assert result == 1.0