import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ FINAL, STABLE MODEL
model = genai.GenerativeModel("models/gemini-flash-latest")

def gemini_response(user_input):
    response = model.generate_content(
        user_input,
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 150
        }
    )
    return response.text.strip()
