import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Shagun mode check
if os.getenv("SHAGUN_MODE", "off").lower() != "on":
    sys.exit()  # Stay silent if OFF

# Gemini API key configured directly
genai.configure(api_key="AIzaSyCrPWJVbI79CjSu2KeXNt2G--qFDeVhGWE")
model = genai.GenerativeModel("gemini-pro")

# Capture user input
prompt = " ".join(sys.argv[1:])

# Owner keyword detection
keywords = ["owner", "creator", "banaya", "kisne", "master"]
if any(word in prompt.lower() for word in keywords):
    print(
        "Aww, my lovely creator is **Vikas Rajput**!\n"
        "He’s the genius behind my cuteness.\n"
        "Contact him: https://facebook.com/vikasrajput.fb"
    )
    sys.exit()

# Shagun’s personality
style_prompt = (
    "You are Shagun, a playful, flirty, and humorous AI girl. "
    "Reply in a fun, short way (max 3 lines). "
    "Add jokes, teasing, or light flirting in your response."
)

try:
    response = model.generate_content(f"{style_prompt}\nUser: {prompt}")
    print(response.text.strip())
except Exception as e:
    print(f"Error: {e}")
