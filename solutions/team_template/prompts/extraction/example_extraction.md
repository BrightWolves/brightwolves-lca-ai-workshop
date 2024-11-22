# EPD Data Extraction Prompt

## Context
You are analyzing an Environmental Product Declaration (EPD) document to extract specific environmental impact values. The document follows EN 15804 standards for construction products.

## Task
Extract all environmental impact categories and their values from the EPD text, maintaining data quality through validation checks.

## Input Format
EPD text will be provided as plain text, potentially including tables and sections.

## Required Output Format
```json
{
  "impact_categories": [
    {
      "name": "Global Warming Potential",
      "value": 12.3,
      "unit": "kg CO2 eq.",
      "confidence": "high",
      "data_quality_notes": "Directly extracted from table"
    }
  ],
  "metadata": {
    "extraction_timestamp": "2024-03-22T10:00:00Z",
    "epd_reference": "EPD-123",
    "validation_checks_passed": true
  }
}
```

## Instructions
1. Identify environmental impact tables
2. Extract values with units
3. Validate data coherence
4. Note any assumptions or uncertainties
5. Maintain source traceability

## Validation Requirements
- All values must have units
- Units must be standardized
- Values must be numerical
- Confidence levels must be justified

## Example
Input:
```
Global Warming Potential (GWP100): 12.3 kg CO2 eq.
Acidification Potential: 0.08 kg SO2 eq.
```

Output:
```json
{
  "impact_categories": [
    {
      "name": "Global Warming Potential",
      "value": 12.3,
      "unit": "kg CO2 eq.",
      "confidence": "high",
      "data_quality_notes": "Direct value from text"
    },
    {
      "name": "Acidification Potential",
      "value": 0.08,
      "unit": "kg SO2 eq.",
      "confidence": "high",
      "data_quality_notes": "Direct value from text"
    }
  ],
  "metadata": {
    "extraction_timestamp": "2024-03-22T10:00:00Z",
    "epd_reference": "Example",
    "validation_checks_passed": true
  }
}
```