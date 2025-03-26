from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🔹 Gemini API Key
GEMINI_API_KEY = "AIzaSyDI7Vpgpac-kw5TvYTqIU-9u88aynAMGps"

# 🔹 Gemini API Call Function
def get_gemini_response(user_input):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}

    payload = {
        "contents": [
            {
                "parts": [{"text": user_input}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload, params=params)
    
    if response.status_code == 200:
        return response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response")
    else:
        return f"Error: {response.json()}"

# 🔹 AI Chat Route
@app.route("/chat", methods=["GET"])
def chat():
    user_message = request.args.get("message")
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response_text = get_gemini_response(user_message)
    
    return jsonify({"reply": response_text})

# 🔹 UptimeRobot Ping Route (Server Active Rakhne Ke Liye)
@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200  # Simple response jo uptime check karega

# 🔹 Server Start
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
