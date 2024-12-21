import torch
from transformers import pipeline
import gradio as gr

# Función para transcribir audio usando el modelo OpenAI Whisper
def transcript_audio(audio_file):
    # Inicializar el pipeline de reconocimiento de voz
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny" , # 'openai/whisper-large',openai/whisper-tiny.en
        chunk_length_s=30,
        device=device
    )
    # Transcribir el archivo de audio y devolver el resultado
    result = pipe(audio_file, batch_size=8)["text"]
    return result

# Configurar la interfaz de Gradio
audio_input = gr.Audio(sources="upload", type="filepath")  # Entrada de audio
output_text = gr.Textbox()  # Salida de texto

# Crear la interfaz de Gradio con la función, entradas y salidas
iface = gr.Interface(fn=transcript_audio, 
                     inputs=audio_input, outputs=output_text, 
                     title="Aplicación de Transcripción de Audio",
                     description="Sube el archivo de audio")

# Lanzar la aplicación de Gradio
iface.launch(server_name="0.0.0.0", server_port=7860, share=False)