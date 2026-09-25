import os
import gradio as gr
from calculator import add, subtract, multiply


def calculate(num1, operation, num2):
    if operation == "Add":
        return add(num1, num2)
    elif operation == "Subtract":
        return subtract(num1, num2)
    elif operation == "Multiply":
        return multiply(num1, num2)
    return "Invalid Operation"


demo = gr.Interface(
    fn=calculate,
    inputs=[
        gr.Number(label="First Number", value=0),
        gr.Dropdown(
            ["Add", "Subtract", "Multiply"],
            label="Operation", value="Add"),
        gr.Number(label="Second Number", value=0),
    ],
    outputs=gr.Number(label="Result"),
    title="CI/CD Python Calculator",
    description="Automated deployment pipeline running via Docker and Render.",
)

if __name__ == "__main__":
    # Render assigns a dynamic port via the PORT environment variable
    server_port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=server_port)