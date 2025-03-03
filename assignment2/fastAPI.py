from fastapi import FastAPI

"""
We can use FastAPI to create a basic HTTP/RESTful API in Python.

assumes that the following packages have been installed useing pip:
1. pip install fastapi
2. pip install uvicorn

Or, we can use the built-in fastapi command to run the API, but we'll need an additional package installation:
1. pip install "fastapi[standard]"

Altnatively, you we can use fastapi diectly from the command line:
1. uvicorn fastAPI:app --reload

"""
app = FastAPI()


# root route
@app.get("/")
def read_root():
    return {"Welcom to SoundBody, please login!"}


@app.get("/api/greet/{musicianName}")
def greet(musicianName: str):
    return {"message": f"Welcome to SoundBody, {musicianName}!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)