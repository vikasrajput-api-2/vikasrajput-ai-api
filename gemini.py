import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def get_shagun_reply(user_message: str) -> str:
    owner_keywords = ['owner', 'malik', 'boss', 'creator']
    if any(word in user_message.lower() for word in owner_keywords):
        owner_name = os.getenv("OWNER_NAME", "Unknown")
        owner_fb = os.getenv("OWNER_FB", "#")
        return f"Mere malik ka naam hai *{owner_name}*\nFacebook: {owner_fb}"

    prompt = f"Reply like a funny, short (max 3 lines) chatbot named Shagun. Don't mention the owner unless asked specifically. Message: \"{user_message}\""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()
        reply = data['candidates'][0]['content']['parts'][0]['text'].strip()
        return reply
    except Exception:
        return "Oops! Shagun thoda so gayi hai, baad mein try karo!"
  
