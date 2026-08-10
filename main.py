from fastapi import FastAPI

app = FastAPI(title = "BATCH 555-B API")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/name")
def read_name():
    return {"name": "Prudhvi"}

@app.get("/batch")
def batch():
    return {"batch": "555B"}

@app.get("/mail")
def get_mail():
    return {"MAIL": "sprudhvi120@gmail.com"}