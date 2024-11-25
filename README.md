# brightwolves-lca-ai-workshop

Workshop materials for accelerating Life Cycle Analysis (LCA) using AI/LLM tools. Created by BrightWolves for VTK/Emergent students.

## Overview

This workshop demonstrates how Large Language Models (LLMs) can enhance Life Cycle Assessment (LCA) efficiency and accuracy. Through hands-on exercises, participants will explore using AI to accelerate:

- Data extraction from technical documentation
- Nomenclature harmonisation across datasets
- Missing data inference
- Impact classification automation
- Documentation standardisation

## Prerequisites

- Basic Python programming knowledge
- Understanding of [LCA concepts](https://www.brightwolves.com/post/life-cycle-assessment-lcas-a-powerful-tool-for-extended-producer-responsibility-epr-compliance)
- Basic understanding of [Git](https://git-scm.com/docs/user-manual) and access to [GitHub](https://github.com/) (ideally with your own account)
- API access (instructions provided)

## Quick Start

1. **Prerequisites**
   ```bash
   # Install [uv package manager](https://docs.astral.sh/uv/)
   curl -LsSf https://astral.sh/uv/install.sh | sh  # Unix/macOS
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows
   ```

2. **Clone & Setup**
   ```bash
   # Fork repo via GitHub interface first, then:
   git clone https://github.com/BrightWolves/brightwolves-lca-ai-workshop.git
   cd brightwolves-lca-ai-workshop
   
   # Add upstream remote
   git remote add upstream https://github.com/brightwolves/brightwolves-lca-ai-workshop.git
   ```

3. **Environment Setup**
   ```bash
   # Create and activate environment
   uv venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   
   # Install core dependencies
   uv pip install -r requirements.txt
   
   # Optional: Install development tools
   uv pip install -r requirements-dev.txt  # Adds testing, linting, docs tools
   
   # Setup environment variables
   cp .env.template .env
   # Edit .env with your API keys
   ```

   The dependencies are split into two files:
   - `requirements.txt`: Core packages needed for the workshop exercises
   - `requirements-dev.txt`: Additional tools for testing, code quality, and documentation

   We recommend installing both during the workshop to take advantage of:
   - Code formatting (`black`)
   - Type checking (`mypy`)
   - Testing tools (`pytest`)
   - Documentation generation (`mkdocs`)

4. **Create Team Environment**
   ```bash
   # Create feature branch
   git checkout -b feature/team_XX_setup  # Replace XX with team number
   
   # Copy template
   cp -r solutions/team_template solutions/team_XX
   
   # Commit setup
   git add solutions/team_XX
   git commit -m "team_XX: Initial setup"
   git push origin feature/team_XX_setup
   ```

5. **Create Pull Request**
   - Go to GitHub repository
   - Create PR from your feature branch to main
   - Fill in PR template
   - Request review

## Development Flow

1. **Start New Exercise**
   ```bash
   # Update main
   git checkout main
   git pull upstream main
   
   # Create feature branch
   git checkout -b feature/team_XX_exercise_YY
   ```

2. **Work on Exercise**
   - Code in your team's directory
   - Commit frequently
   - Push to share with team
   - Run tests locally

3. **Submit Solution**
   - Create PR via GitHub
   - Follow PR template
   - Request review
   - Address feedback

## Common Issues

1. **Environment**
   ```bash
   # If uv fails, fallback to pip:
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Git Issues**
   ```bash
   # Reset local changes
   git checkout -- .
   
   # Update from upstream
   git fetch upstream
   git reset --hard upstream/main
   ```

## Workshop Structure

### 1. Introduction (20 min)
- LCA fundamentals
- AI/LLM integration opportunities
- Tool overview

### 2. Hands-on Exercise (80 min)
Teams work on mineral wool insulation case study:
- Exercise 1 (20 min): Data extraction
- Exercise 2 (25 min): Processing and analysis
- Exercise 3 (25 min): Results analysis and visualisation

### 3. Results Discussion (20 min)
- Team presentations
- Best practices, implementation considerations, key learnings
- Next steps

## Next Steps
1. Complete environment setup
2. Read exercise documentation
3. Start first exercise

## Repository Structure

```
brightwolves-lca-ai-workshop/.
├── data/                           # Workshop datasets and templates
│   ├── example_epd.txt            # Sample EPD documents
│   └── output_templates/          # Output format templates for exercises
│
├── exercises/                      # Workshop exercise materials
│   ├── 01_data_extraction/        # EPD data extraction exercise
│   ├── 02_data_processing/        # Data processing and analysis
│   ├── 03_analysis/              # Results analysis and visualization
│   ├── 04_Validation/            # Data validation framework
│   └── setup_env.py              # Environment setup utilities
│
├── solutions/                      # Team solution workspaces
│   ├── team_template/             # Template for team solutions -- clone this and replace the content with your solutions to the excercises
│   │   ├── notebooks/            # Team's exercise notebooks
│   │   ├── prompts/             # LLM prompt templates
│   │   ├── src/                 # Source code implementation
│   │   └── tests/               # Team-specific tests
│
├── docs/                          # Documentation and guides
│   ├── APIServicesGuide.md       # API setup and usage guide
│   └── repository_structure.md    # Detailed folder structure guide
```

## Development Workflow

We follow trunk-based development with the `main` branch as our trunk. All changes are made through short-lived feature branches and merged via Pull Requests.

### Initial Setup

1. **Fork and Clone**
   ```bash
   # Fork via GitHub interface, then:
   git clone https://github.com/your-username/brightwolves-lca-ai-workshop.git
   cd brightwolves-lca-ai-workshop
   ```

2. **Set Up Remote**
   ```bash
   git remote add upstream https://github.com/brightwolves/brightwolves-lca-ai-workshop.git
   ```

### Team Workflow

1. **Start Fresh**
   ```bash
   # Get latest changes
   git checkout main
   git pull upstream main
   
   # Create short-lived feature branch
   git checkout -b feature/team_XX_exercise_YY
   ```

2. **Copy Template** (first time only)
   ```bash
   cp -r solutions/team_template solutions/team_XX
   ```

3. **Regular Commits**
   ```bash
   # Stage and commit changes
   git add solutions/team_XX
   git commit -m "team_XX: Brief description of changes"
   
   # Push to your fork
   git push origin feature/team_XX_exercise_YY
   ```

4. **Create Pull Request**
   - Create PR via GitHub interface
   - Use the PR template
   - Target the `main` branch
   - Include:
     - Team members
     - Exercise description
     - Approach summary
     - Test results

5. **Review Process**
   - PR needs one approval
   - All checks must pass
   - Keep changes focused and small
   - Address review comments promptly

6. **After Merge**
   ```bash
   # Delete local feature branch
   git checkout main
   git branch -D feature/team_XX_exercise_YY
   
   # Update local main
   git pull upstream main
   ```

### Branch Naming Convention

- Format: `feature/team_XX_exercise_YY`
- Example: `feature/team_01_data_extraction`

### Commit Message Format

```
team_XX: Brief description of change

- Detailed point 1
- Detailed point 2
```

### PR Title Format

```
team_XX: Exercise YY - Brief Description
```

1. **Create Team Branch**
   ```bash
   git checkout -b [team_XX]
   ```

2. **Copy Template**
   ```bash
   cp -r solutions/team_template_solutions/[team_XX]
   ```

3. **Submit Solution**
   ```bash
   git add solutions/[team_XX]
   git commit -m "Team XX: Solution submission"
   git push origin [team_XX]
   ```

4. **Create Pull Request**
   - Use provided template
   - Include team details
   - Document approach

## Resources
 - [LCA Background]([link-to-resources](https://www.brightwolves.com/post/life-cycle-assessment-unveiling-iso-standards-gfli-in-our-newest-whitepaper-series)) 
 - API Documentation
   + [Anthropic](https://docs.anthropic.com/en/home)
   + [OpenAI](https://openai.com/api/)

## Getting Help

- Technical issues: [Open GitHub Issue](https://github.com/BrightWolves/brightwolves-lca-ai-workshop/issues)
- Workshop questions: [Use Discussion board](https://github.com/BrightWolves/brightwolves-lca-ai-workshop/discussions)
- Emergency: Contact workshop lead

## License

This project is licensed under the MIT License with Attribution - see the [LICENSE](LICENSE) file for details.

## Citation

If you use these materials in your work, please cite:

```bibtex
@software{brightwolves_lca_ai_2024,
  author = {BrightWolves},
  title = {LCA AI Workshop},
  year = {2024},
  url = {https://github.com/brightwolves/brightwolves-lca-ai-workshop}
}
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

## Acknowledgments

- [Emergent Leuven](https://emergentleuven.be/) and [Vlaamse Technische Kring (VTK)](https://vtk.be/) for collaboration
- Workshop participants for feedback
- Open-source tools and libraries used

## Contact

For questions about this workshop or BrightWolves' LCA services:
- Email: [info@brightwolves.eu](mailto:info@brightwolves.eu)
- Website: [brightwolves.com](https://brightwolves.com)
- 
# API Keys
- OpenAI I
sk-proj-rPn6XA_ai-Vv51DsewebRnWK9ERA80_AfRON3Nu_somMjj2OADdO8mMEoaxI8TN4GWhsxUGGFOT3BlbkFJGBAR74SJih-
- OpenAI II
uhFWTRnSq0TxkvWbv_B__hFvc1u4tFStSwSUc9qib_gLF4Y7xrU4_K3saeNylAA 
# Anthropic I
sk-ant-api03-9d2k9k2GUotqlrwE_lJf95ccrhqcyGvpscC72ZhpV3SUjjr5hA-
# Anthropic II
kuB4hGfQJyxBZaK-0lFdtI-He8FkpuudH4g-Xq1M8gAA
