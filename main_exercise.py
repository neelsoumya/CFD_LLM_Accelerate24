from openai import OpenAI
import dotenv
import os
from rich import print as rprint

dotenv.load_dotenv()

# Global parameters
MAX_NUM_TOKENS_RESPONSE = 1000

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

print("Simple prompt \n")
print(response.choices[0].message.content)
print("*******************************************\n")

# give it prompt v2
# chain of thought prompting
#   https://docs.science.ai.cam.ac.uk/hands-on-llms/prompting/3_prompting/#piagets-glass-of-water
system_prompt = "You are an expert on computational fluid dynamics and gas turbine and ducted fan design"
user_query = "Can you please tell me how to optimize efficiency of a ducted fan for a drone? Assume you have access to the diffusion factor for flow through the turbine. Please step through your reasoning and explain all the steps in your reasoning. For example, start byd efining efficiency, then determine how diffusion factor will affect efficiency, then determine how to change diffusion factor. Please provide references and links to justify your arguments."

response = client.chat.completions.create(
    model= "gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": user_query},
    ],
    max_tokens=MAX_NUM_TOKENS_RESPONSE
) 

print("*******************************************\n")
print("Chain of thought prompting \n")
print(response.choices[0].message.content)
print("*******************************************\n")
