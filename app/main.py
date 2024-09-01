from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "We Love Datascientest, and we did it. We build a CI/CD Pipeline - Test Automation #3 -> Modification d'adresse IP à cause de la nouvelle vm DST-fastapi"}
