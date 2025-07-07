from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="FastAPI Prompt AI Backend",
    description="Login, submit prompts, get AI responses, and view prompt history.",
    version="1.0.0"
)

app.include_router(router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Prompt AI Backend! Visit /docs for API documentation."}
