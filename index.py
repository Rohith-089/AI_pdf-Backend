from fastapi import FastAPI
from route.pdf import router as pdf_router

app = FastAPI(title="AI PDF Summarizer")

app.include_router(pdf_router)

@app.get("/")
def root():
    return {"message": "Welcome to AI PDF Summarizer API"}
