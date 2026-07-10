import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-3.1-flash-lite")

import re

def generate_code(prompt, language, framework):

    full_prompt = f"""
You are an expert software engineer.

Generate clean, production-ready code.

Language: {language}

Framework: {framework}

User Request:
{prompt}

IMPORTANT:
- Return ONLY the source code.
- Do NOT explain anything.
- Do NOT use markdown.
- Do NOT wrap the code inside triple backticks.
"""

    response = model.generate_content(full_prompt)

    code = response.text.strip()

    # Remove opening ```python or ```java etc.
    code = re.sub(r"^```[a-zA-Z0-9_+-]*\n?", "", code)

    # Remove ending ```
    code = re.sub(r"\n?```$", "", code)

    return code.strip()