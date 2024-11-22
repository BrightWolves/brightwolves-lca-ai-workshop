# EPD Data Extraction

## Context
Extracting environmental impact data from EPD document.

## Task
Extract standardized impact categories and values.

## Input Format
EPD text with tables and sections.

## Output Format
```json
{
  "impact_categories": [],
  "metadata": {}
}
```

## Validation Rules
- Values must be numerical
- Units must be present
- Confidence levels required
