from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    text = data['text']
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400
    
    return jsonify(result)

    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)