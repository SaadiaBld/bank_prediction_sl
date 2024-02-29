from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, prediction 
from database import Database
from person import Person
from http.client import HTTPException
from enum import Enum
from fastapi.templating import Jinja2Templates 

app = FastAPI()

class Features(Enum):
    NAICS = 'naics'
    Term = 'term' 
    NewExist = 'newexit'
    UrbanRural = 'urbanrural' 
    RevLineCr = 'revlinecr'
    LowDoc = 'lowdoc'

class PredictionOutput(BaseModel):
    category:int

model = load_model()

database = Database()

FEATURES = [{'NAICS': '', 'Term': '', 'NewExist': '', 'UrbanRural': '', 'RevLineCr': '', 'LowDoc': ''}]

@app.get("/features")
async def features() -> list[dict]:
    return FEATURES

@app.get("/features/{features_id}", status_code=206)
async def features(features_id: int) -> str:
    features = next((b for b in features if b['id'] == features_id), None)
    if features is None :
        raise HTTPException(status_code=404, detail='features not found')
    return features

@app.get('/features/genre/{genre}') 
async def features_for_genre(genre: Features) -> list[dict]:
    return [b for b in FEATURES if b['genre'].lower() == genre.lower()]


@app.head("/api/persons/")
async def toto():
    return database.head() 

@app.get("/api/persons/")
async def index(nom):
    return {"hello": "world"}


@app.get("/api/persons")
def list_persons():
    return database.list_records()

@app.get("/api/persons/{person_id}")
def read_persons(person_id: int):
    return database.read(person_id)


@app.get("/api/persons/")
def read_NAICS(person_id: int):
    return database.read()

@app.get("/")
async def home() -> dict[str, str]:
    return {'name': 'louis'}


@app.get('/about')
async def about(): 
    return 'an exceptional'

@app.post("/predict")
async def predict(payload: Person):
    features = [value for value in payload.dict().values()]
    predictions = prediction(model, [features])
    return {"predictions": "predictions"}
