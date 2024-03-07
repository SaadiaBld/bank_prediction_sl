from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, prediction
from http.client import HTTPException
from enum import Enum
from fastapi.templating import Jinja2Templates 
from joblib import load 

app = FastAPI()
model = load_model()



# Modèle Pydantic pour la structure de données d'entrée
class FeaturesInput(BaseModel):
    Term: float 
    FranchiseCode: float 
    UrbanRural: float 
    RevLineCr: str
    LowDoc: str
    GrAppv: int
    SBA_Appv: int
    NAICS_digit: int 


class PredictionOutput(BaseModel):
    category:int


@app.post('/predict')
def prediction_root(feature_input:FeaturesInput):
    F1=feature_input.Term
    F2=feature_input.FranchiseCode
    F3=feature_input.UrbanRural
    F4=feature_input.RevLineCr
    F5=feature_input.LowDoc
    F6=feature_input.GrAppv
    F7=feature_input.SBA_Appv
    F8=feature_input.NAICS_digit 
    
    pred = prediction(model,[[F1,F2,F3,F4,F5,F6,F7,F8]])
    
    return PredictionOutput(category=pred)


"""
### Facultatif
# Liste pour stocker les items
items_db = []

# récupère toutes les caractéristiques de l'items (NAICS, Term, NewExist, UrbanRural, RevLineCr, LowDoc)
@app.get("/items/")
async def get_items():
    return items_db

# récupère un items par son ID
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail='Item not found')

# mettre à jour un item existant par son ID
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: FeaturesInput):
    for index, db_item in enumerate(items_db):
        if db_item["id"] == items_db:
            items_db[index] = item.dict()
            items_db[index]["id"] = item_id 
            return {"": "Item updtate successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

# supprimer item existant par son id
@app.delete("/items/{items_id}")
async def delete_item(item_id: int):
    for index, db_item in enumerate(items_db):
        if db_item["id"] == item_id:
            del items_db[index]
            return {"message": "Item supprimé avec succès"}
    raise HTTPException(status_code=404, detail="Item non trouvé")

# supprimer une personne dont l'id est déjà passé 
app.delete("/api/items/{item_id}")
def delete_item(item_id: int):
    items_db.delete(FeaturesInput)
"""