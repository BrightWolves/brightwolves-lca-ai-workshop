class EPDExtractor:
    """Base class for EPD data extraction with pre-implemented helpers."""
    
    def __init__(self, model_name: str = "claude-3-5-sonnet-latest"): # Currently latest is claude-3-5-sonnet-20241022 at time of writing
        self.model = model_name
        self.extraction_prompt = load_prompt("extraction/base_prompt.md")
    
    def extract_from_pdf(self, pdf_path: str) -> dict:
        """Extract structured data from EPD PDF."""
        text = self._extract_text(pdf_path)
        tables = self._extract_tables(pdf_path)
        return self._process_content(text, tables)
    
    def validate_extraction(self, data: dict) -> tuple[bool, list[str]]:
        """Validate extracted data against known patterns."""
        # Pre-implemented validation logic
        pass

