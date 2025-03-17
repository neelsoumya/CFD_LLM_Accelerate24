from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import LLM
import uvicorn

app = FastAPI()

# Initialize the LLM model
model_name = "gpt2"  # You can replace this with any other model available on Hugging Face Hub
llm = LLM(model_name=model_name)

class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 50

class TextGenerationResponse(BaseModel):
    generated_text: str

@app.post("/generate-text", response_model=TextGenerationResponse)
def generate_text(request: TextGenerationRequest):
    try:
        prompt = llm.preprocess_input(request.prompt)
        generated_text = llm.generate_text(prompt, max_length=request.max_length)
        generated_text = llm.postprocess_output(generated_text)
        return TextGenerationResponse(generated_text=generated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)