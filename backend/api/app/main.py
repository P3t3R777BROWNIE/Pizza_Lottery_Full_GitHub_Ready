
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Pizza Lottery API running"}

@app.get("/health")
def health():
    return {"status": "ok"}
