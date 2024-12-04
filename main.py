from openai import OpenAI
import dotenv
import os
import pandas as pd
from rich import print as rprint

dotenv.load_dotenv()
client = OpenAI()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

system_prompt = """
You are an expert in turbomachinery.
Use your experience in aeronautical engineering to think try to gather insights from the data."""


user_query = "Testing."

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query},
    ],
    max_tokens=128
)

print(response.choices[0].message.content)