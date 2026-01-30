from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Minha API Simples")

class EchoIn(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello(name: str = "world"):
    return {"message": f"hello, {name}"}

@app.get("/sum")
def sumab(a:int, b:int):
        return {"result": a+b}

@app.post("/echo")
def echo(payload: EchoIn):
    return {"text": payload.text, "length": len(payload.text)}