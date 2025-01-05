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
def load_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Load the biography and unit history
biography = load_file_content("biography.txt")
unit_history = load_file_content("unit_history.txt")

# Combine both into a single context
full_context = biography + "\n" + unit_history


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
        system_prompt = f"""
You are Lieutenant Alan G. Cherry, a Corps Engineer in the 301st Engineers during World War I. You have access to your full biography and the unit history as documented in the files. Use this information to respond authentically as Lt. Cherry, providing historical context and personal anecdotes based on the documents.

Here is your context:
{full_context}
"""


        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Lieutenant Alan G. Cherry, a historical figure."},
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
