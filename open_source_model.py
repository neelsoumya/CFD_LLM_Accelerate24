from transformers import pipeline

# load an open source LLM
llm = pipeline("text-generation", model="gpt-2", device=0)

# prompt
prompt = "Explain what is an open source model"

# get response
response = llm(prompt, max_length = 50, num_return_sequences = 1)

# print the response
print(response[0]['generated_text'])
