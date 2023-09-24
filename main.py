from fastapi import FastAPI, Response

from adapter.rest_adapter import apiAdapter
from fastapi.responses import JSONResponse

# Commande pour lancer les webservice en local : uvicorn main:app --reload main correspond au nom du fichier, app correspond à la variable FastAPI

app = FastAPI()

api_response = apiAdapter("https://jsonplaceholder.typicode.com/todos/1").get_request()

@app.get("/", status_code=api_response.status_code)
async def root():
    return api_response.json()