# Repository Guide

## Prompt Engineering and Management

### Structure
- `prompts/` directory in team folders for version control of prompts
- Each prompt type has its own file (extraction.md, validation.md, etc.)
- Prompts are treated like code: reviewed, tested, and versioned
- A good example is given here: solutions/team_template/prompts/extraction/example_extraction.md

### Prompt Types
```
prompts/
├── extraction/             # EPD data extraction
│   ├── base_prompt.md     # Core extraction strategy
│   └── refinements/       # Specific field extractors
├── validation/            # Data validation
│   ├── unit_checks.md    
│   └── completeness.md
└── reporting/             # Documentation generation
    └── summary.md
```

### Best Practices
1. **Version Control**
   - Track prompt changes in git
   - Document why prompts were modified
   - Keep prompt history for comparison

2. **Testing**
   ```python
   def test_extraction_prompt():
       """Test prompt against known EPD data"""
       result = run_prompt('prompts/extraction/base_prompt.md', test_epd)
       assert_extracted_fields(result)
   ```

3. **Documentation**
   - Note which model version used
   - Track performance metrics
   - Document edge cases

### Example Prompt Structure
```markdown
# Data Extraction Prompt

## Context
Extracting data from Environmental Product Declaration (EPD)

## Task Description
Extract specific environmental impact values and units

## Required Format
JSON with fields:
- impact_category
- value
- unit
- confidence

## Example Input/Output
[Examples of successful extractions]

## Additional Instructions
- Handle unit conversions
- Note data quality
- Flag uncertainties
```

## Project Organization

### Notebooks vs. Source Code

The project uses both Jupyter notebooks (`.ipynb`) and Python source files (`.py`) for different purposes:

**Notebooks (`notebooks/`)**: Interactive development and exploration
- `01_environment_setup.ipynb`: Verify tool installation and API access
- `02_data_extraction.ipynb`: Explore EPD document parsing techniques
- `03_data_processing.ipynb`: Develop data cleaning and analysis approaches
- `04_visualization.ipynb`: Create and refine visualizations

**Source Code (`src/`)**: Reusable, tested implementation
- `extraction.py`: Clean functions for extracting data from EPDs
- `processing.py`: Data transformation and LCI calculations
- `validation.py`: Data quality checks and result validation
- `visualization.py`: Plotting functions for standard visualizations

**Why This Split?**
- Notebooks: Experimentation, visualization, learning
- Source: Clean, documented, tested code
- Best practice: Develop in notebooks, refactor to source
- Enables proper testing and version control

## Code Quality Tools Explained

- **Formatting (black)**: Ensures consistent code style across all teams
- **Linting (ruff)**: Catches common mistakes and enforces best practices
- **Type Checking (mypy)**: Prevents type-related bugs before they occur
- **Testing (pytest)**: Verifies code works as intended
- **Coverage**: Measures test completeness by tracking executed code

## Key Files

### Configuration Files
- `pyproject.toml`: Project metadata and tool configurations (black, ruff, mypy, pytest)
- `.env.template`: Template for API keys and configuration
- `.gitignore`: Specifies which files Git should ignore

### Dependency Management
- `requirements.txt`: Core dependencies for workshop exercises
- `requirements-dev.txt`: Additional tools for development
  - Documentation generators
  - Testing utilities
  - Code quality tools

### GitHub Templates
- `.github/PULL_REQUEST_TEMPLATE/`: PR submission guidelines
- `.github/ISSUE_TEMPLATE/`: Bug report and feature request templates

### Team Workspace
```
solutions/team_XX/
├── src/              # Source code
├── tests/            # Test cases
├── notebooks/        # Jupyter notebooks
└── README.md         # Team documentation
```

## Development Tools

### Code Quality
```bash
# Format code - Automatically fixes code style to match project standards
black solutions/team_XX

# Lint code - Checks for potential errors, style violations, and code smells
ruff check solutions/team_XX

# Type checking - Verifies correct usage of data types to prevent runtime errors
mypy solutions/team_XX
```

### Testing
```bash
# Run tests - Executes test suite to verify code functionality
pytest solutions/team_XX/tests

# With coverage - Shows which lines of code are executed during tests
# Helps identify untested code paths
pytest --cov=solutions/team_XX
```

### Documentation
```bash
# Generate docs
mkdocs serve
```

## Dependencies

### Core (`requirements.txt`)
- Data processing: pandas, numpy
- Visualization: matplotlib, seaborn
- PDF handling: pdfplumber, PyPDF2
- API integration: requests, anthropic, openai

### Development (`requirements-dev.txt`)
- Testing: pytest, pytest-cov
- Formatting: black, ruff
- Type checking: mypy
- Documentation: mkdocs

## Environment Variables
Required in `.env`:
```
ANTHROPIC_API_KEY=your_key
OPENAI_API_KEY=your_key
PERPLEXITY_KEY=your_key
```

## Best Practices
- Keep notebooks clean and documented
- Run code quality tools before commits
- Update team README with approach details
- Include tests for core functionality