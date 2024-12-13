import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base",force_download=True)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base",force_download=True)

def caption_image(input_image: np.ndarray):
    # Convert numpy array to PIL Image and convert to RGB
    image = Image.fromarray(input_image).convert('RGB')
    
    # Process the image
    text = "the image of"
    inputs = processor(images=image, text=text, return_tensors="pt")

    # Generate a caption for the image
    outputs = model.generate(**inputs, max_length=50)

    # Decode the generated tokens to text and store it into `caption`
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return caption

iface = gr.Interface(
    fn=caption_image, 
    inputs=gr.Image(), 
    outputs="text",
    title="Image Captioning",
    description="This is a simple web app for generating captions for images using a trained model."
)

iface.launch(server_name="0.0.0.0", server_port= 7860, share=True)