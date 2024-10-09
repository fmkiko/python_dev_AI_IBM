from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
# Initialize the processor and model from Hugging Face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")# cargar un procesador preestrenado de Hugging Face
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")# cargar un modelo preestrenado de Hugging Face
# Load an image
path_img = r'C:\Users\Francisco Martínez\Pictures\Saved Pictures\dog.png'
image = Image.open(path_img)

# Prepare the image
inputs = processor(image, return_tensors="pt")# prepara la img para pytorch -> pt
# Generate captions
outputs = model.generate(**inputs)
caption = processor.decode(outputs[0],skip_special_tokens=True)
 
print("Generated Caption:", caption)
