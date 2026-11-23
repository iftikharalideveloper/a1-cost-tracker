import os
import sys
import json
import time

from dotenv import load_dotenv
from google import genai
from groq import Groq

# Load environment variables from .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GEMINI_MODEL = os.getenv("GEMINI_MODEL")
GROQ_MODEL = os.getenv("GROQ_MODEL")


# Check required environment variables
required_variables = {
    "GEMINI_API_KEY": GEMINI_API_KEY,
    "GROQ_API_KEY": GROQ_API_KEY,
    "GEMINI_MODEL": GEMINI_MODEL,
    "GROQ_MODEL": GROQ_MODEL,
}

for variable, value in required_variables.items():
    if not value:
        print(f"Error: {variable} is missing from .env")
        sys.exit(1)


# Prices in USD per 1 million tokens
GEMINI_INPUT_PRICE = 0.75
GEMINI_OUTPUT_PRICE = 3.75

GROQ_INPUT_PRICE = 0.15
GROQ_OUTPUT_PRICE = 0.60


def call_gemini(prompt):
    client = genai.Client(api_key=GEMINI_API_KEY)

    start_time = time.perf_counter()

    response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)

    elapsed = time.perf_counter() - start_time

    reply = response.text or ""

    usage = response.usage_metadata

    if usage is None:
        raise RuntimeError("Gemini did not return token usage information.")

    input_tokens = usage.prompt_token_count
    output_tokens = usage.candidates_token_count

    if input_tokens is None or output_tokens is None:
        raise RuntimeError("Gemini token counts are missing.")

    return reply, input_tokens, output_tokens, elapsed


def call_groq(prompt):
    client = Groq(api_key=GROQ_API_KEY)

    start_time = time.perf_counter()

    response = client.chat.completions.create(
        model=GROQ_MODEL, messages=[{"role": "user", "content": prompt}]
    )

    elapsed = time.perf_counter() - start_time

    reply = response.choices[0].message.content or ""

    usage = response.usage

    if usage is None:
        raise RuntimeError("Groq did not return token usage information.")

    input_tokens = usage.prompt_tokens
    output_tokens = usage.completion_tokens
    if input_tokens is None or output_tokens is None:
        raise RuntimeError("Groq token counts are missing.")

    return reply, input_tokens, output_tokens, elapsed


def calculate_cost(input_tokens, output_tokens, input_price_per_m, output_price_per_m):
    input_cost = (input_tokens * input_price_per_m) / 1_000_000

    output_cost = (output_tokens * output_price_per_m) / 1_000_000

    total_cost = input_cost + output_cost

    return total_cost


def run_tracker(prompt):
    results = []

    providers = [
        {
            "name": "gemini",
            "model": GEMINI_MODEL,
            "function": call_gemini,
            "input_price": GEMINI_INPUT_PRICE,
            "output_price": GEMINI_OUTPUT_PRICE,
        },
        {
            "name": "groq",
            "model": GROQ_MODEL,
            "function": call_groq,
            "input_price": GROQ_INPUT_PRICE,
            "output_price": GROQ_OUTPUT_PRICE,
        },
    ]

    for provider in providers:
        print(f"\nCalling {provider['name']}...")

        try:
            reply, input_tokens, output_tokens, elapsed = provider["function"](prompt)

            cost = calculate_cost(
                input_tokens,
                output_tokens,
                provider["input_price"],
                provider["output_price"],
            )

            result = {
                "provider": provider["name"],
                "model": provider["model"],
                "reply": reply,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "input_price_per_m": provider["input_price"],
                "output_price_per_m": provider["output_price"],
                "cost_usd": cost,
                "seconds": round(elapsed, 3),
            }

            results.append(result)

            print(f"\n--- {provider['name'].upper()} REPLY ---")
            print(reply)

        except Exception as error:
            print(f"Error with {provider['name']}: {error}")

    return results


def display_results(results):
    print("\n========== COST COMPARISON ==========")

    print(
        f"{'Provider':<12}"
        f"{'Input Tokens':<15}"
        f"{'Output Tokens':<16}"
        f"{'Seconds':<12}"
        f"{'Cost (USD)':<12}"
    )

    print("-" * 67)

    for result in results:
        print(
            f"{result['provider']:<12}"
            f"{result['input_tokens']:<15}"
            f"{result['output_tokens']:<16}"
            f"{result['seconds']:<12}"
            f"${result['cost_usd']:.8f}"
        )


def save_results(results):
    with open("results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

    print("\nResults saved to results.json")


def main():
    if len(sys.argv) < 2:
        print('Usage: uv run tracker.py "your prompt"')
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])

    results = run_tracker(prompt)

    if not results:
        print("\nNo successful provider responses. Results not saved.")
        sys.exit(1)

    display_results(results)
    save_results(results)


if __name__ == "__main__":
    main()
