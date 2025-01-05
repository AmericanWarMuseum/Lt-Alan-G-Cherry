from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

# Create the Flask app
app = Flask(__name__)
CORS(app)

# Load your OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load Lt. Cherry's biography
def load_biography():
    try:
        with open('cherry_bio.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Biography not found."

# Load the unit history
def load_unit_history():
    try:
        with open('unit_history.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Unit history not found."

# Define the /chat route to handle user messages
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
        You are Lieutenant Alan G. Cherry, a veteran of the 301st Engineers in World War I. You were born in the late 1800s, and your experiences are documented in your biography and unit history. You must respond in character as Lt. Cherry at all times.

        Here is your personal biography:
        {biography}

        Here is your unit history:
        {unit_history}

        The user is asking about a specific event, time period, or personal memory. Refer to your biography or unit history to answer their question in detail.

        Respond as Lt. Cherry:
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error occurred:", e)
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
