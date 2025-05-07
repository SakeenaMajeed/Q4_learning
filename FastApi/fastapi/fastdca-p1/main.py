from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Sakeena():
    return "Hello World 🌎"
