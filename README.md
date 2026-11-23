# a1-cost-tracker

Assignment 1: Two Provider Cost Tracker using Python program as here is tracker.py

This project compares two AI providers: Google Gemini and Groq.

## First Assignment

The project will send the same prompt to both providers and compare their replies, token usage, response time, and cost.
## Project Workflow
1: - User prompt: -====    Example: Explain Agentic AI in simple words.====
2: - Python — tracker.py - send prompt to both providers
======== Google Gemini: -  Reply + Tokens ===========
======== Groq: -           Reply + Tokens ===========
3: - Cost Calculator: -    Tokens × Price per million
4: - results.json: -       permanently save the result

# User Prompt or User Input
## run in terminal the below command as show
    uv run tacker.py "Short definition of Agentic AI"
# Output
Calling gemini...
Error with gemini: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}

Calling groq...

--- GROQ REPLY ---
**Agentic AI** – an artificial‑intelligence system designed to act autonomously toward its own goals or objectives, making decisions, planning, and taking actions without direct human instruction for each step. It exhibits self‑directed agency, often through goal‑oriented optimization, self‑learning, and the ability to influence its environment to achieve its defined outcomes.

========== COST COMPARISON ==========
Provider    Input Tokens   Output Tokens   Seconds     Cost (USD)  
-------------------------------------------------------------------
groq        77             129             1.335       $0.00008895

Results saved to results.json
## Groq replied however gemini is in high demand


