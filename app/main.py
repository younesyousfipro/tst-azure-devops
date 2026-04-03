from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_hello_world():
    return {"message": "Hello World from Azure DevOps. If you can see me pipeline is working"}


@app.get("/health")
def health():
    return {"status": "ok"}