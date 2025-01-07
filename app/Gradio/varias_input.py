import gradio as gr

def combine(a, b):
    return a + " " + b

demo = gr.Interface(
    fn=combine,
    inputs = [
        gr.Textbox(label="Entrada 1"),
        gr.Textbox(label="Entrada 2")
    ],
    outputs = gr.Textbox(value="", label="Salida")
)
demo.launch(server_name="0.0.0.0", server_port= 7860)