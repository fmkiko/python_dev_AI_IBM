import torch
import os
import gradio as gr

#from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub

from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

mis_credenciales = {
    "url"    : "https://us-south.ml.cloud.ibm.com"
}
params = {
        GenParams.MAX_NEW_TOKENS: 800, # El número máximo de tokens que el modelo puede generar en una sola ejecución.
        GenParams.TEMPERATURE: 0.1,   # Un parámetro que controla la aleatoriedad de la generación de tokens. Un valor más bajo hace que la generación sea más determinista, mientras que un valor más alto introduce más aleatoriedad.
    }

LLAMA2_model = Model(
        model_id= 'meta-llama/llama-3-8b-instruct', 
        credentials=mis_credenciales,
        params=params,
        project_id="skills-network",  
        )

llm = WatsonxLLM(LLAMA2_model)  

#######------------- Plantilla de Prompt-------------####
# This template is structured based on LLAMA2. If you are using other LLMs, feel free to remove the tags
temp = """
<s><<SYS>>
Enumera los puntos clave con detalles del contexto: 
[INST] El contexto : {context} [/INST] 
<</SYS>>
"""
# here is the simplified version of the prompt template
# temp = """
# List the key points with details from the context: 
# The context : {context} 
# """

pt = PromptTemplate(
    input_variables=["context"],
    template= temp)

prompt_to_LLAMA2 = LLMChain(llm=llm, prompt=pt)

#######------------- De voz a texto-------------####

def transcript_audio(audio_file):
    # Inicializa el pipeline de reconocimiento de voz
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )
    # Transcribe el archivo de audio y devuelve el resultado
    transcript_txt = pipe(audio_file, batch_size=8)["text"]
    result = prompt_to_LLAMA2.run(transcript_txt)

    return result

#######------------- Gradio-------------####

audio_input = gr.Audio(sources="upload", type="filepath")
output_text = gr.Textbox()

iface = gr.Interface(fn= transcript_audio, 
                    inputs= audio_input, outputs= output_text, 
                    title= "Aplicación de Transcripción de Audio",
                    description= "Sube el archivo de audio")

iface.launch(server_name="0.0.0.0", server_port=7860)