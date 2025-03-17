from model import LLM

# Initialize the LLM model
model_name = "gpt2"  # You can replace this with any other model available on Hugging Face Hub
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