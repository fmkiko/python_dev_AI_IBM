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
    pip install transformers==4.30.2 torch

4. **Verify the installation**:
    ```bash
    pip list
    ```
# Crate new file python and imports and model to use
chatbot.py
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = "facebook/blenderbot-400M-distill" #  you'll be using facebook/blenderbot-400M-distill because it has an open-source license and runs relatively fast.
# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)




