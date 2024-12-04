import os
import dotenv
import pandas as pd
import nn_based_prediction as ml
from openai import OpenAI
from rich import print as rprint

class llm_based_prediction:

    def initial_prediction(self):
        # Load OpenAI key for LLM prompting.
        dotenv.load_dotenv()
        client = OpenAI()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

        # Create base LLM prompts; will be edited later.
        system_prompt = """
        You are an expert in turbomachinery.
        Use your experience in aeronautical engineering to think try to gather insights from the data.
        """
        user_query = "Testing."

        # Run LLM.
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query},
            ],
            max_tokens=1024
        )

        print(response.choices[0].message.content)