def test_epd_extraction():
    """Test extraction of key fields from sample EPD."""
    extractor = EPDExtractor()
    result = extractor.extract_from_pdf("data/reference_results/sample_epd.pdf")
    assert "impact_categories" in result
    # Add more specific test cases