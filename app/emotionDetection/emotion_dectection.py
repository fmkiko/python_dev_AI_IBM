import requests, json


# primer con text
import requests

def emotion_detector(text_to_analyze):
    # URL and headers  
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Prepare the input to send in json
    data_json = { "raw_document": { "text": text_to_analyze } }

    try:
        # Send the POST request
        response = requests.post(URL, headers=headers, json=data_json)

        if response.status_code == 200:
            # Retunr the 'text' from the response
            result = response.text 
            return result
        else:
            return { "error": { "status_code": response.status_code, "msg": response.text}}
    except Exception as e:
        return f"Error: {str(e)}"
    


def emotion_detector(text_to_analyze):
    # URL and headers  
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Prepare the input to send in json
    data_json = { "raw_document": { "text": text_to_analyze } }

    try:
        # Send the POST request
        response = requests.post(URL, headers=headers, json=data_json)

        if response.status_code == 200:
            # Retunr the 'text' from the response
            result = response.json() 
            return result.get('emotionPredictions')[0].get('emotion')
        else:
            return { "error": { "status_code": response.status_code, "msg": response.text}}
    except Exception as e:
        return f"Error: {str(e)}"
    
# result = emotion_detector("I love this new technology.")
# print(result)
'''
    abre la shell de python
    python3.11
    from emotion_detection import emotion_detector
    result = emotion_detector("I love this new technology.")
    print(result)
'''

def emotion_detector(text_to_analyze):
    # URL and headers  
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Prepare the input to send in json
    data_json = { "raw_document": { "text": text_to_analyze } }

    try:
        # Send the POST request
        response = requests.post(URL, headers=headers, json=data_json)

        if response.status_code == 200:
            # Convert the response text into a dictionary
            result = json.loads(response.text)

            # Extract the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores.
            emotion = emotion = result.get('emotionPredictions')[0].get('emotion')
            emotion_scores = {
                'anger': emotion.get('anger', 0),
                'disgust': emotion.get('disgust', 0),
                'fear':  emotion.get('fear', 0),
                'joy': emotion.get('joy', 0),
                'sadness': emotion.get('sadness', 0)
            }

            # Write the code logic to find the dominant emotion, which is the emotion with the highest score.
            emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)
            
            return emotion_scores
        else:
            return { "error": { "status_code": response.status_code, "msg": response.text}}
    except Exception as e:
        return f"Error: {str(e)}"