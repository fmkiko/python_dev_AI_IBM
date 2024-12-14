# pip install git+https://github.com/openai/whisper.git
import whisper

# Cargar el modelo
model = whisper.load_model("base")

# Ruta del archivo de audio (usa 'r' para evitar problemas con caracteres especiales)
audio = r"C:\Users\Francisco Martínez\Documents\filePython\app\create IA app coursera IBM\whisper\audio_example.mp3"

# Transcribir el archivo
result = model.transcribe(audio)

# Imprimir la transcripción
print(result["text"])