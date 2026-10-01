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

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"API Error: {str(e)}"
