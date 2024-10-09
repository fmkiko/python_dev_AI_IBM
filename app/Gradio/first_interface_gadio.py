import gradio as gr

def greet(saludo, name, intensity):
    return saludo + " " + name + "!" * int(intensity)

demo = gr.Interface(
    fn = greet,
    inputs = ["text", "text", "slider"],
    outputs = ["text"]
)

demo.launch()