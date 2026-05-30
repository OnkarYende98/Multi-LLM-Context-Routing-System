import google.generativeai as genai

from groq import Groq

from config import (
    GEMINI_API_KEY,
    GROQ_API_KEY
)

# -------------------------
# Gemini Setup
# -------------------------

genai.configure(
    api_key=GEMINI_API_KEY
)

gemini_model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# -------------------------
# Groq Setup
# -------------------------

groq_client = Groq(
    api_key=GROQ_API_KEY
)


def ask_gemini(prompt):

    try:

        response = gemini_model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {str(e)}"


def ask_groq(prompt):

    try:

        response = groq_client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Groq Error: {str(e)}"