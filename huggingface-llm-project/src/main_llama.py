from model import LLM
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the Hugging Face API token as an environment variable
os.environ["HUGGINGFACE_HUB_TOKEN"] = os.getenv("HUGGINGFACE_HUB_TOKEN")

# Initialize the LLM model
model_name = "meta-llama/Llama-2-7b"  # Replace this with the latest Llama model available on Hugging Face Hub
llm = LLM(model_name=model_name)

def generate_text(prompt, max_length=50):
    try:
        prompt = llm.preprocess_input(prompt)
        generated_text = llm.generate_text(prompt, max_length=max_length)
        generated_text = llm.postprocess_output(generated_text)
        return generated_text
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    prompt = "Once upon a time"
    max_length = 50
    generated_text = generate_text(prompt, max_length)
    if generated_text:
        print("Generated Text:")
        print(generated_text)