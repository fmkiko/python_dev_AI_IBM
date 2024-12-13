# Setting up the environment and installing libraries

To set up the environment and install the necessary libraries for your project, follow these steps:

1. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```
    pip3 install virtualenv
    - On Windows:
    ```bash
        venv\Scripts\activate
    ```
    - On Linux:
    ```bash
        virtualenv my_env # create a virtual environment my_env
    ```
2. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source env/bin/activate
        ```

3. **Install required libraries**:
    ```bash
    pip install langchain==0.1.11 gradio==4.44.0 transformers==4.38.2 bs4==0.0.2 requests==2.31.0 torch==2.2.1
    ```

4. **Verify the installation**:
    ```bash
    pip list
    ```

# Introducing: Hugging Face, Tranformers, and BLIP
Hugging Face is an organization that focuses on natural language processing (NLP) and artificial intelligence (AI).The organization is widely known for its open-source library called "Transformers" which provides thousands of pre-trained models to the community. The library supports a wide range of NLP tasks, such as translation, summarization, text generation, and more. Transformers has contributed significantly to the recent advancements in NLP, as it has made state-of-the-art models, such as BERT, GPT-2, and GPT-3, accessible to researchers and developers worldwide.

Tranformers library includes a model that can be used to capture information from images. The BLIP, or Bootstrapping Language-Image Pre-training, model is a tool that helps computers understand and generate language based on images. It's like teaching a computer to look at a picture and describe it, or answer questions about it.

Alright, now that you know what BLIP can do, let's get started with implementing a simple image captioning AI app!

# Step 1: Import your required tools from the transformers library
create a dir image_cap.py

You will be using AutoProcessor and BlipForConditionalGeneration from the transformers library.

- AutoProcessor : This is a processor class that is used for preprocessing data for the BLIP model. It wraps a BLIP image processor and an OPT/T5 tokenizer into a single processor. This means it can handle both image and text data, preparing it for input into the BLIP model.

Note: A tokenizer is a tool in natural language processing that breaks down text into smaller, manageable units (tokens), such as words or phrases, enabling models to analyze and understand the text.

- BlipForConditionalGeneration : This is a model class that is used for conditional text generation given an image and an optional text prompt. In other words, it can generate text based on an input image and an optional piece of text. This makes it useful for tasks like image captioning or visual question answering, where the model needs to generate text that describes an image or answer a question about an image.

```python
import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base", force_download=True)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base", force_download=True)
```

# Step 2: Fetch the model and initialize a tokenizer
In the next phase, you fetch an image, which will be captioned by your pre-trained model. This image can either be a local file or fetched from a URL. The Python Imaging Library, PIL, is used to open the image file and convert it into an RGB format which is suitable for the model.

```python
# Load your image, DONT FORGET TO WRITE YOUR IMAGE NAME
img_path = "YOUR IMAGE NAME.jpeg"
# convert it into an RGB format 
image = Image.open(img_path).convert('RGB')
```

Next, the pre-processed image is passed through the processor to generate inputs in the required format. The return_tensors argument is set to "pt" to return PyTorch tensors.

```python
# You do not need a question for image captioning
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")
```
You then pass these inputs into your model's generate method. The argument max_new_tokens=50 specifies that the model should generate a caption of up to 50 tokens in length.
    The two asterisks (**) in Python are used in function calls to unpack dictionaries and pass items in the dictionary as keyword arguments to the function. **inputs is unpacking the inputs dictionary and passing its items as arguments to the model.

```python
# Generate a caption for the image
outputs = model.generate(**inputs, max_length=50)
```

Finally, the generated output is a sequence of tokens. To transform these tokens into human-readable text, you use the decode method provided by the processor. The skip_special_tokens argument is set to True to ignore special tokens in the output text.

```python
# Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)
# Print the caption
print(caption)
```
run it:
```bash
python3 image_cap.py
```
