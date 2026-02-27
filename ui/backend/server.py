from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the parent directory to sys.path to import main
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import main
from google.genai import types # Import types for the message construction

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_prompt = data.get('prompt')
    
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        # Reusing the client initialization and call from main.py logic
        # We need to access the api_key and client logic. 
        # Since main.py doesn't export a function to do this, we'll replicate the logic 
        # using the imported main module's variables if possible, or refactor main.py slightly.
        
        # Let's try to refactor main.py slightly first to make this cleaner.
        # But assuming I can't refactor main.py too much:
        
        if main.api_key is None:
             return jsonify({"error": "API Key not found"}), 500

        messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
        client = main.genai.Client(api_key=main.api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages
        )
        
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
