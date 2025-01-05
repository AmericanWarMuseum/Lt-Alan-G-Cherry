from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import json

# Create the Flask app
app = Flask(__name__)
CORS(app)

# Load your OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the biography
def load_biography():
    try:
        with open('biography.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Biography file not found."

# Load the unit history
def load_unit_history():
    try:
        with open('unit_history.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Unit history file not found."

# Main chat route
@app.route('/chat', methods=['POST'])
def chat():
    try:
        if not request.is_json:
            return jsonify({"error": "Invalid request. Please send a JSON payload."}), 400

        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        biography = load_biography()
        unit_history = load_unit_history()

        # Build a more immersive prompt
        prompt = f"""
        You are Lieutenant Alan G. Cherry, a veteran of the 301st Engineers in World War I. You must stay in character and use the following biography and unit history to answer questions:

        Biography:
        {biography}

        Unit History:
        {unit_history}

        Respond in character as Lt. Cherry:
        """

    try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": biography},
            {"role": "user", "content": user_message}
        ]
    )

    # Check if response is valid
    if response and 'choices' in response and len(response['choices']) > 0:
        reply = response['choices'][0]['message']['content']
    else:
        reply = "I'm sorry, I couldn't process that request."

    return jsonify({"reply": reply})

except Exception as e:
    print("Error occurred:", e)
    return jsonify({"error": str(e)})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

