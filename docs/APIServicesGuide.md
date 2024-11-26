# API Services Guide

## Available Services

### Anthropic (Claude)
```
ANTHROPIC_API_KEY=your_key
```
- Best for: Complex reasoning, code understanding, step-by-step analysis
- Strengths: Document analysis, consistent structured output, careful validation
- Use when: Extracting detailed EPD data, validating calculations, generating documentation
- Models: Claude 3.5 Sonnet (balanced and currently best), Claude 3: Opus (largest) and Haiku (fastest)

### OpenAI (GPT and o1)
```
OPENAI_API_KEY=your_key
```

**GPT Models**
- Best for: Quick data processing, format conversion, summarization
- Strengths: Fast responses, good with standard formats, broad knowledge
- Use when: Rapid prototyping, simple data transformations, unit conversions
- Models: GPT-4 (most capable), GPT-3.5 (faster, cost-effective)

**o1 Models** (New Reasoning Series)
- o1-preview
  - Best for: Complex scientific analysis, advanced math, multi-step reasoning
  - Strengths: Thorough problem-solving, high accuracy in technical tasks
  - Use when: Complex LCA calculations, methodology validation, technical documentation
  - Rate limit: 50 queries/week
  
- o1-mini
  - Best for: Coding tasks and logical reasoning
  - Strengths: Cost-effective, efficient for programming
  - Use when: Developing data processing scripts, optimization tasks
  - Rate limit: 50 queries/day
  - Cost: 80% cheaper than o1-preview

### Perplexity
```
PERPLEXITY_KEY=your_key
```
- Best for: Research, fact checking, current data verification
- Strengths: Up-to-date information, citations, research synthesis
- Use when: Verifying EPD standards, checking methodologies, finding references, literature search
- Models: pplx-7b-online (fast), pplx-70b-online (more capable)

## Alternative Options
- **Local Models**: Consider installing [Ollama](https://ollama.com/) to load and run Llama 3.2 for fully local processing if your hardware supports the configurations
- **Other Services**: Google Gemini family offers competitive capabilities with exceptionally large context windows
- **Open Models**: Hugging Face and other Model Zoos provide self-hostable options

## Suggested Usage Strategy
1. Initial extraction and/or complex reasoning: Claude 3.5 Sonnet or o1-preview (thorough, structured)
2. Quick validations: GPT or Haiku (fast turnaround)
3. Standards/references: Perplexity (current information)
4. Code development: o1-mini (cost-effective) combineed with Claude 3.5 Sonnet or o1-preview for more complex

## Cost Optimisation
- Prototype with GPT-3.5/Haiku
- Use Chlaude 3.5 Sonnet/o1-preview for final validation
- Cache responses for repeated queries
- Consider local models for high-volume tasks