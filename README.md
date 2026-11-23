# Two Provider Cost Tracker

**Assignment 1 — Phase 1: Foundations**

A Python-based LLM cost tracker that sends the same prompt to two AI providers — Google Gemini and Groq — and compares their responses, token usage, response time, and estimated API cost.

## Project Overview

The purpose of this project is to understand how different LLM providers can be integrated into one Python application and how their token usage and costs can be measured.

The application:

- Sends the same user prompt to Google Gemini and Groq.
- Displays each provider's response.
- Retrieves actual input and output token counts from API usage metadata.
- Measures response time.
- Calculates estimated API cost.
- Displays a side-by-side comparison.
- Saves successful results in `results.json`.

## Technologies Used

- Python 3.14+
- Google Gemini API (`google-genai`)
- Groq API (`groq`)
- `python-dotenv` for environment variables
- `uv` for Python project and dependency management
- Git and GitHub for version control

## Project Structure

```text
a1-cost-tracker/
│
├── tracker.py          # Main application
├── results.json        # Saved API results
├── .env                # Private API keys (not committed)
├── .env.example        # Example environment configuration
├── .gitignore          # Excludes private and temporary files
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock             # Locked dependency versions
├── .python-version     # Python version configuration
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/iftikharalideveloper/a1-cost-tracker.git
```

```bash
cd a1-cost-tracker
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template.

Add your own API keys and model names:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
GROQ_API_KEY=your_actual_groq_api_key

GEMINI_MODEL=your_gemini_model_name
GROQ_MODEL=your_groq_model_name
```

Never commit your actual `.env` file or share API keys publicly.

### 4. Run the application

```bash
uv run tracker.py "Explain Agentic AI in one simple sentence."
```

## Cost Calculation

The application calculates the estimated cost using the following formula:

**Input Cost**

```text
(input_tokens × input_price_per_m) / 1,000,000
```

**Output Cost**

```text
(output_tokens × output_price_per_m) / 1,000,000
```

**Total Cost**

```text
input_cost + output_cost
```

The configured prices are in USD per one million tokens.

| Provider |       Input price |      Output price |
| -------- | ----------------: | ----------------: |
| Gemini   | $0.75 / 1M tokens | $3.75 / 1M tokens |
| Groq     | $0.15 / 1M tokens | $0.60 / 1M tokens |

These are the pricing values configured in the application. Actual charges may depend on provider pricing, model, and free-tier eligibility.

## Example Test Result

The following is an actual successful test using:

```text
Explain Agentic AI in one simple sentence.
```

Both providers returned a response successfully.

| Metric         |        Gemini |          Groq |
| -------------- | ------------: | ------------: |
| Input tokens   |            10 |            80 |
| Output tokens  |            34 |            64 |
| Response time  | 6.886 seconds | 0.788 seconds |
| Estimated cost |   $0.00013500 |   $0.00005040 |

### Example Responses

**Gemini:**

Agentic AI is artificial intelligence that can independently plan, make decisions, and take action to achieve a specific goal without needing step-by-step human guidance.

**Groq:**

Agentic AI is an artificial intelligence system that can autonomously make decisions and take actions to achieve its own defined goals.

## Results Storage

After successful provider calls, the application saves the results in `results.json`.

Each successful provider result contains:

- `provider`
- `model`
- `reply`
- `input_tokens`
- `output_tokens`
- `input_price_per_m`
- `output_price_per_m`
- `cost_usd`
- `seconds`

The JSON file is overwritten with the latest successful run.

## Development Process & Implementation History

This section documents the actual development and testing process followed while building the assignment.

### 1. Repository and Environment Setup

Created the GitHub repository and cloned it to the local Windows development environment.

Configured the Python project using `uv` and installed the required dependencies.

### 2. API Provider Configuration

Integrated two different LLM providers:

- Google Gemini
- Groq

Configured API keys and model names through environment variables in `.env`.

Added `.env.example` so that the required configuration can be understood without exposing private credentials.

### 3. API Integration and Token Tracking

Implemented separate functions for both providers.

Each function sends the same user prompt, retrieves the response, reads the provider's actual token usage metadata, and measures elapsed time.

Added validation to handle missing token usage information.

### 4. Cost Calculator

Implemented a reusable cost calculation function.

It calculates input and output costs separately and combines them to produce the total estimated cost in USD.

### 5. Result Comparison and JSON Storage

Implemented the provider orchestration, terminal comparison table, and JSON result storage.

The application handles provider errors individually so that one provider's failure does not automatically prevent the other provider from being called.

### 6. Troubleshooting Gemini API Availability

During initial testing, the Gemini API returned a `503 UNAVAILABLE` high-demand error with the initially configured model.

To investigate the issue, an alternative Gemini model was configured: `gemini-3.6-flash`.

Subsequent testing confirmed successful Gemini responses.

Groq was also tested successfully using `openai/gpt-oss-120b`.

### 7. Final Testing and Verification

Ran multiple tests to verify:

- Both provider integrations.
- Actual API token usage.
- Cost calculation.
- Response-time measurement.
- JSON result generation.
- Python syntax.
- Dependency synchronization.
- Git whitespace checks.
- Environment-file exclusion from Git tracking.

The final meaningful test returned successful responses from both Gemini and Groq.

## Security

The project uses environment variables to protect API credentials.

The `.gitignore` file excludes:

```text
.env
.venv/
__pycache__/
```

The `.env.example` file contains placeholders only.

## Assignment Goal

This project demonstrates the fundamentals of:

- Integrating multiple LLM providers.
- Working with API responses and usage metadata.
- Tracking input and output tokens.
- Calculating estimated API costs.
- Measuring response time.
- Managing environment variables and API credentials.
- Saving structured results in JSON.
- Using Git and GitHub for version control.

---

**Repository:** [https://github.com/iftikharalideveloper/a1-cost-tracker](https://github.com/iftikharalideveloper/a1-cost-tracker)

**Assignment:** Assignment 1 — Two Provider Cost Tracker