from transformers import AutoModelForCausalLM, LlamaTokenizer
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the Hugging Face API token as an environment variable
os.environ["HUGGINGFACE_HUB_TOKEN"] = os.getenv("HUGGINGFACE_HUB_TOKEN")

from huggingface_hub import login
login(token = os.getenv("HUGGINGFACE_HUB_TOKEN"))


# Initialize the Llama model and tokenizer
model_name = "meta-llama/Llama-2-7b"  # Replace with the desired Llama model
tokenizer = LlamaTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

def generate_text(prompt, max_length=50):
    """
    Generate text using the Llama model.
    :param prompt: Input prompt for the model
    :param max_length: Maximum length of the generated text
    :return: Generated text
    """
    try:
        # Tokenize the input prompt
        inputs = tokenizer(prompt, return_tensors="pt")
        
        # Generate text
        outputs = model.generate(**inputs, max_length=max_length)
        
        # Decode the generated text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
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
