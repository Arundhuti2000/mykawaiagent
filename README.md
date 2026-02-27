# My Kawai Agent

A small AI agent project using the Google Gemini API.

## Description

This project demonstrates a simple implementation of an AI agent using the `google-genai` library. It connects to the Gemini 2.5 Flash model to generate content based on text prompts.

## Prerequisites

- Python 3.x
- A Google Gemini API Key

## Setup

1.  **Clone the repository** (if applicable)

2.  **Install dependencies**

    Make sure you have the required packages installed. You can install them using `pip` or `uv`.

    ```bash
    pip install google-genai python-dotenv
    # or if using uv
    uv add google-genai python-dotenv
    ```

3.  **Environment Configuration**

    Create a `.env` file in the root directory and add your Gemini API key:

    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

To run the agent, execute the `main.py` script:

```bash
python main.py
# or if using uv
uv run main.py
```

## Features

- connects to Google's Gemini 2.5 Flash model
- Reports token usage (prompt and response tokens)

## Calculator Module

This project also includes a simple command-line calculator.

### Usage

To use the calculator, run the `calculator/main.py` script with a mathematical expression:

```bash
python calculator/main.py "3 + 5 * (10 - 2)"
# Output:
# {
#   "expression": "3 + 5 * (10 - 2)",
#   "result": 43
# }
```

### Supported Operations

- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`
- Parentheses `()` for grouping
