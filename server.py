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

# Search the unit history for the user's query
def search_unit_history(query):
    try:
        with open('unit_history.txt', 'r') as file:
            text = file.read()
            if query.lower() in text.lower():
                start = text.lower().index(query.lower())
                end = start + 500  # Return 500 characters around the query
                return text[start:end]
            else:
                return "I don't have information on that specific topic."
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
        relevant_text = search_unit_history(user_message)

        prompt = f"""
        You are Lt. Alan G. Cherry, a World War I veteran. Here is your personal biography:
        {biography}

        The user is asking about a specific event or detail. Here is the relevant text from your unit history:
        {relevant_text}

        Please respond to the user's query:
        {user_message}
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
