import google.generativeai as genai
from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

# Use free-tier fast model
model = genai.GenerativeModel("gemini-1.5-flash")

def gemini_generate(prompt):
    response = model.generate_content(prompt)
    return response.text
