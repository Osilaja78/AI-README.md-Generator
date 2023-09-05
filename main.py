from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import g4f
from pydantic import BaseModel

app = FastAPI(title="AI README.md generator")

# Enable CORS middleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "My AI README.md generator Backend"}

class RequestData(BaseModel):
    repoName: str
    repoDescription: str

@app.post("/ask_gpt")
async def ask_gpt(request: RequestData):

    messages = []

    prompt = f"Repository: ${request.repoName}\nDescription: ${request.repoDescription}\nGenerate\
            a README.md file with installation and usage instructions:\n"
    messages.append({"role": "user", "content": prompt})
    print(messages)
    
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        provider=g4f.Provider.DeepAi,
        messages=messages,
    )

    return {"response": response}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)