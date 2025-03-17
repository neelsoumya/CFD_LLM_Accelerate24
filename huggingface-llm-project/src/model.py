from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLM:
    def __init__(self, model_name):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_text(self, prompt, max_length=50):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def preprocess_input(self, input_text):
        # Add any preprocessing steps if necessary
        return input_text.strip()

    def postprocess_output(self, output_text):
        # Add any postprocessing steps if necessary
        return output_text.strip()