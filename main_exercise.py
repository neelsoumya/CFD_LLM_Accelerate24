from openai import OpenAI
import dotenv
import os
from rich import print as rprint

dotenv.load_dotenv()

# API call
client = OpenAI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# give it prompt
system_prompt = "You are an expert on computational fluid dynamics and gas turbine and ducted fan design"
user_query = "Can you please tell me how to optimize efficiency of a ducted fan for a drone?"

response = client.chat.completions.create(
    model= "gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": user_query},
    ],
    max_tokens=128
) 

print(response.choices[0].message.content)