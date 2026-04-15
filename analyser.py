from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_message(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are a cybersecurity assistant.
Give output in this format:

Risk Level:
Reason:
Advice:"""
            },
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content
