from fastapi import FastAPI
from pydantic import BaseModel
from model import generate_text

app = FastAPI()

class TextRequest(BaseModel):
    prompt: str
    max_length: int = 50

@app.post("/generate/")
async def generate(request: TextRequest):
    generated_text = generate_text(request.prompt, request.max_length)
    return {"generated_text": generated_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)