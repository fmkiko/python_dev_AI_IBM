# dir app
app/
    create IA app coursera IBM/
        LAB3_voice_gpt3/
            chatapp-with-voice-and-openai/
                Dockerfile
                requirements.txt
                certs/
                    rootCA.crt
                models/
                    stt/
                        README.md
                        Dockerfile
                        prepareModels.sh
                        chuck_var/
                            env_config.json
                    tts/
                        README.md
                        Dockerfile
                        prepareModels.sh
                        config/
                            env_config.json
                static/
                    script.js
                    style.css
                templates/
                    index.html
                server.py

# Model IBM WATSON VOICE TO TEXT AND TEXT TO VOICE (STT, TTS) prerequisites
For voice to text and text to voice conversion we use IBM Watson. 
You must have an IBM account and the appropriate permissions to sing the API.

# worker.py you can find the function to conversion voice

- Function speech_to_text(audio_binary):

    The function simply takes audio_binary as the only parameter and then sends it in the body of the HTTP request.

    To make an HTTP Post request to the Watson Speech-to-Text API, you need the following:

    API URL: This is defined as api_url in your code and points to Watson's Speech-to-Text service.
    Parameters: This is defined as params in your code. It is simply a dictionary that has a key-value pair, i.e. 'model': 'en-US_Multimedia', which simply tells Watson that you want to use the US English model to process your speech.
    Request Body: This is defined as body and is equal to audio_binary, as you are sending the audio data within the body of your POST request.
    Then you use requests library to send this HTTP request passing the url, params and data (body) to it and then use .json() to convert the API response to json format which is very easy to parse and can be treated like a dictionary in Python.

    The structure of the response is as follows:
    ```json
        {
        "response": {
            "results": {
            "alternatives": {
                "transcript": "Recognised text from your speech"
            }
            }
        }
    }
    ```

- Function text_to_speech(text, voice=""):

    The function simply takes text and voice as parameters. It adds the voice as a parameter to the api_url if it is not empty or default. It sends the text in the body of the HTTP request.

    Similarly, as before, to make an HTTP Post request to the Watson Text-to-Speech API, you need the following three elements:

    API URL: This is defined as api_url in your code and points to Watson's Text to Speech service. This time you also add a voice parameter to the api_url if the user has submitted a preferred voice in their request.
    Headers: This is defined as headers in your code. It is just a dictionary that has two key-value pairs. The first is ‘Accept’:’audio/wav’ which tells Watson that we are sending an audio in wav format. The second is ‘Content-Type’:’application/json’ which means that the body format will be JSON.
    Request body: This is defined as json_data and is a dictionary containing the key-value pair ‘text’:text, this text will be processed and converted to audio.
    We then use the requests library to send this HTTP request passing the URL, headers and json(body) to it and then use .json() to convert the API response to json format so we can parse it.

    The structure of the response is something like this:
    ```json
        {
          "response": {
            content: The Audio data for the processed text to speech
          }
        }
    ```


# Integrating the OpenAI API
You must have an openAi api key.

#  worker.py you can find the function openai_process_message(user_message):
This is where you can give your personal assistant some personality. In this case, you're telling the model to become a personal assistant by: Act like a personal assistant, and then giving it specific tasks that it's capable of: You can respond to questions, translate sentences, summarize news, and give recommendations.. By adding the user's original message afterwards, you give OpenAI more room to sound genuine. Feel free to change this as needed.

You then call the OpenAI API using the openai.chat.completions.create function and pass the following 3 parameters:

model: This is the OpenAI model we want to use to process our prompt, in this case we're using their gpt-3.5-turbo model.
messages: The messages parameter is an array of objects used to define the conversation flow between the user and the AI. Each object represents a message with two key attributes: role (identifying the sender as “system” for configuration instructions or “user” for the actual user query) and content (the text of the message). The “system” role message instructs the AI ​​on how to behave (e.g., acting as a personal assistant), while the “user” role message contains the user input. This structured approach helps personalize AI responses to be more relevant and personalized.
max_tokens: This is the maximum response length we are looking for. 30 tokens corresponds to roughly 1-2 sentences. Right now, we are setting it to 4000, which is the maximum token value this model supports.
Again, you can definitely tune these parameters to your custom needs, and you can learn more about them by visiting the OpenAI playground where you can try out all the parameters in real time.

The response structure goes something like this:
```json
    {
        "choices": [
            {"message": {
                content: "The model\'s answer to our prompt",
                ...,
                ...,
            },
            ...,
            ...
            ]
    }
```

# Running the app with docker
```bach
docker build . -t voice-chatapp-powered-by-openai
docker run -p 8000:8000 voice-chatapp-powered-by-openai
``` 







