from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, prediction

model = load_model()

# Modèle Pydantic pour la structure de données d'entrée
class Features(BaseModel):
    NAICS: int = 0
    Term: int = 0
    NewExist: int = 0
    Franchise_code: int = 0
    UrbanRural: int = 0
    RevLineCr: int = 0
    LowDoc: int = 0

    def __init__(self, NAICS) -> 0:
        self.NAICS = NAICS

    def __init__(self, Term) -> 0:
        self.Term = Term
    
    def __init__(self, NewExist) -> 0:
        self.NewExist = NewExist
    
    def __init__(self, Franchise_code) -> 0:
        self.Franchise_code = Franchise_code
    
    def __init__(self, UrbanRural) -> 0:
        self.UrbanRural = UrbanRural
    
    def __init__(self, RevLineCr) -> 0:
        self.RevLineCr = RevLineCr
    
    def __init__(self, LowDoc) -> None:
        self.LowDoc = LowDoc

class PredictionOut(BaseModel):
    category : float

@app.post("/predict")
async def predict(payload: Features):
    features = [value for value in payload.dict().values()]
    predictions = predict_prod(model, [features])
    return PredictionOut(predictions=predictions)



