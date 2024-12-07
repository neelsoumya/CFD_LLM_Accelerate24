from transformers import pipeline

# load an open source LLM
generator = pipeline("text-generation", model="gpt-2")

# give prompt
str_prompt = "Once upon a time"

output = generator(str_prompt, max_length = 100, num_return_sequences = 1)

# print
print(output[0]["generated_text"])

