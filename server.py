from flask import Flask, request, jsonify, send_from_directory
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
    with open('cherry_bio.txt', 'r') as file:
        return file.read()

# Search the unit history for the user's query
def search_unit_history(query):
    with open('unit_history.txt', 'r') as file:
        text = file.read()
        if query.lower() in text.lower():
            start = text.lower().index(query.lower())
            end = start + 500  # Return 500 characters around the query
            return text[start:end]
        else:
            return "I don't have information on that specific topic."

# Define the /chat route to handle user messages
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Ensure the request has JSON content
        if not request.is_json:
            return jsonify({"error": "Invalid request. Please send a JSON payload."}), 400

        # Get the user's message from the request
        user_message = request.json.get('message')

        # Handle the case where 'message' is not provided
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Load the biography
        biography = load_biography()

        # Search the unit history
        relevant_text = search_unit_history(user_message)

        # Build the prompt
        prompt = f"""
        You are Lt. Alan G. Cherry, a World War I veteran. Here is your personal biography:
        {biography}

        The user is asking about a specific event or detail. Here is the relevant text from your unit history:
        {relevant_text}

        Please respond to the user's query:
        {user_message}
        """

        # Send the prompt to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_message}
            ]
        )

        # Get the AI's reply
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except Exception as e:
        # Print the error to the terminal
        print("Error occurred:", e)
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
