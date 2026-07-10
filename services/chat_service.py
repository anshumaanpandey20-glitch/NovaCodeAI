import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "models/gemini-3.1-flash-lite"
)

chat = model.start_chat(history=[])


def chat_with_ai(message):

    response = chat.send_message(message)

    return response.text