from transformers import pipeline

# Load a small open-source model for text generation
generator = pipeline("text-generation", model="gpt2")

# Generate text based on a prompt
prompt = "Once upon a time"
output = generator(prompt, max_length=50, num_return_sequences=1)

# Print the generated text
print(output[0]["generated_text"])
