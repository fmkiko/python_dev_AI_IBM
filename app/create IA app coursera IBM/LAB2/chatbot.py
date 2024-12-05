from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name) #it is an instance of the class AutoModelForSeq2SeqLM, which allows you to interact with your chosen language model 
tokenizer = AutoTokenizer.from_pretrained(model_name)#it is an instance of the class AutoTokenizer, which allows you to tokenize your input text so that it can be processed by the model

# Keeping track of conversation history
# The conversation history is important when interacting with a chatbot because the chatbot will also reference the previous conversations when generating output.
conversation_history = []
# # Initially history is empty
# # The transformers library function you are using expects to receive the conversation history as a string, with each element separated by the newline character '\n'.
# history_string = "\n".join(conversation_history)
# # Fetch prompt from user
# input_text ="hello, how are you doing?"
# # Tokenize input text
# inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
# #print(inputs) # that is a dictionary with the keys 'input_ids', 'attention_mask', and 'token_type_ids'

# # Generate model output
# outputs = model.generate(**inputs)
# #print(outputs)# now you have your outputs! However, the current output outputs is also a dictionary and contains tokens, not words in plaintext.

# # Decode model output
# response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
# #print(response)

# # Add input and response to conversation history
# conversation_history.append(input_text)
# conversation_history.append(response)
# print(conversation_history)

# Repeat
while True:
    # Create conversation history string
    history_string = "\n".join(conversation_history)

    # Get the input data from the user
    input_text = input("> ")

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
    print(inputs)
    # Generate the response from the model
    outputs = model.generate(**inputs)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    print(response)

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)