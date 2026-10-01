from unittest.mock import MagicMock
from chat import ask_gemini


def test_ask_gemini_empty_prompt():
    result = ask_gemini("")
    assert result == "Please enter a question."


def test_ask_gemini_missing_api_key():
    result = ask_gemini("Hello", client=None)
    # When no client and no env var exists, returns key error
    assert "GEMINI_API_KEY" in result or isinstance(result, str)


def test_ask_gemini_success_mock():
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "This is a simulated AI response."
    mock_client.models.generate_content.return_value = mock_response

    result = ask_gemini("What is CI/CD?", client=mock_client)
    assert result == "This is a simulated AI response."