import requests
import json

def emotion_detector(text_to_analyze):
    # URL and Headers for the Watson NLP Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a POST request to the API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Find the dominant emotion by getting the key with the highest value
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the exact requested format
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }