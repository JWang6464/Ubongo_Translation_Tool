import os
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_translations(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or your custom model ID if you're using a fine-tuned model
        messages=[
            {"role": "system", "content": "You are a translation assistant."},
            {"role": "user", "content": f"Translate the following text into Swahili: {text}"}
        ]
    )
    translation1 = response.choices[0].message['content']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a humorous translation assistant."},
            {"role": "user", "content": f"Translate the following text into Swahili with a humorous tone: {text}"}
        ]
    )
    translation2 = response.choices[0].message['content']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a conversational translation assistant."},
            {"role": "user", "content": f"Translate the following text into Swahili with a conversational tone: {text}"}
        ]
    )
    translation3 = response.choices[0].message['content']

    return translation1, translation2, translation3

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')
    translation1, translation2, translation3 = get_translations(text)
    return jsonify({
        "translation1": translation1,
        "translation2": translation2,
        "translation3": translation3
    })

if __name__ == '__main__':
    app.run(debug=True)
