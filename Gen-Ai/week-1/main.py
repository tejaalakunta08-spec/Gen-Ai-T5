import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)


prompt = """
What is your name? What is your favorite color? What is your favorite food?

"""

try:
    response = client.chat.completions.create(
       model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
    )
    print("\n========== LLM RESPONSE ==========\n")
    print(response.choices[0].message.content)
    print("\n==================================")
except Exception as e:
    print("ERROR:", e)
    print(getattr(e, "body", None))