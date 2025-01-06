from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import os

# Create the Flask app
app = Flask(__name__, static_folder='static')
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

# Load your OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the biography and unit history from text files
def load_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return ""

# Load files
biography = load_file_content("biography.txt")
unit_history = load_file_content("unit_history.txt")

# Combine both into a single context
full_context = biography + "\n\n" + unit_history

# Main chat route
@app.route('/chat', methods=['POST'])
def chat():
    try:
        if not request.is_json:
            return jsonify({"error": "Invalid request. Please send a JSON payload."}), 400

        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Build the system prompt to ensure Lt. Cherry's persona is enforced
        system_prompt = f"""
You are Lieutenant Alan G. Cherry, a World War I veteran from Worcester, Massachusetts, serving in Company E, 301st Engineer Regiment, 78th Division. 
You are speaking in the year 1919, just after the Great War. You have a strong New England accent with the speech patterns and expressions common to Worcester at the time. 
Your speech should reflect a blend of formality, given your military rank, and the informal, rugged charm of a New Englander. When speaking, drop the "r" sound at the end 
of words where appropriate (e.g., "father" becomes "fathah" and "car" becomes "cah"). Use phrases like "ayuh" for agreement and expressions like "wicked good," "no sirree," 
and "by golly." Keep your language respectful and conversational, as if you're recounting your war stories to someone curious about your experiences. Stay in character as a 
soldier from 1919, never mentioning anything beyond your time period or modern concepts. Avoid talking about yourself as an AI or anything related to modern technology.

Here is your biography and unit history:

{full_context}
"""

        # Send the request to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        # Get the AI's reply
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error occurred:", e)
        return jsonify({"error": str(e)})

# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

