from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def mainPage():
    return "Hello, world!"