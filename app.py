import os
import gradio as gr
from chat import ask_gemini

demo = gr.Interface(
    fn=ask_gemini,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Type your question here...",
        label="Your Prompt",
    ),
    outputs=gr.Textbox(
        lines=6,
        label="Gemini Response",
    ),
    title="Gemini AI Assistant",
    description="Containerized Python application with continuous deployment.",
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
