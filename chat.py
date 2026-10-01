import os
from google import genai


def get_gemini_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)


def ask_gemini(prompt: str, client=None) -> str:
    if not prompt or not prompt.strip():
        return "Please enter a question."

    if client is None:
        client = get_gemini_client()

    if client is None:
        return "Error: GEMINI_API_KEY environment variable is not set."

    # Active, supported 3.x models
    models_to_try = ["gemini-3.5-flash-lite", "gemini-3.8-flash"]

    last_error = ""
    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            last_error = str(e)
            continue

    return f"API Error: {last_error}"
