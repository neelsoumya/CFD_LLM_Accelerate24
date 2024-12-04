from openai import OpenAI
import dotenv
import os
from rich import print as rprint # for making fancy outputs

dotenv.load_dotenv()
client = OpenAI()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")