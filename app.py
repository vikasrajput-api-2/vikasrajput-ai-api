from flask import Flask, request, jsonify
from gemini import generate_shagun_reply
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return "Shagun AI Bot is running!"

@app.route('/shagun', methods=['POST'])
def shagun_reply():
    data = request.json
    user_input = data.get('message', '')
    response = generate_shagun_reply(user_input)
    return jsonify({"reply": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
