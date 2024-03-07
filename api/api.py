from fastapi import FastAPI
from model_utils import load_model, predict_prod
from pydantic import BaseModel
from typing import ClassVar
from api.model_utils import Items
import pandas as pd

model = load_model()

app = FastAPI()

# Modèle Pydantic pour la structure de données d'entrée
class FeaturesInput(BaseModel):
    NAICS: int
    Term: float # ou int 
    NewExist: float # ou int 
    FranchiseCode: float # ou int
    UrbanRural: float # ou int
    RevLineCr: float 
    LowDoc: float 

# fonction qui predis l'accord du pret en utilisant le modele entrainé:
def predict_loan(model,data):
    # Convertir la liste de listes en DataFrame
    df = pd.DataFrame(data, columns=['Term', 'FranchiseCode', 'UrbanRural', 'RevLineCr', 'LowDoc', 'GrAppv', 'SBA_Appv', 'NAICS_digit'])
    predictions = model.predict(df)
    return predictions[0]

class PredictionOut(BaseModel):
    predictions : float

"""
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
    
    
class Database:
    def __init__(self) -> None:
        self.__d = dict()
        self.__internal_index = 0

    def create(self, record: features) -> int:
        current_index = self.__internal_index
        self.__d[current_index] = record
        self.__internal_index += 1
        return current_index

    def update(self, index, record: FeaturesInput):
        self.__d[index] = record

    def read(self, index: int) -> FeaturesInput:
        return self.__d[index]

    def delete(self, index):
        del self.__d[index]

    def list_records(self) -> list[FeaturesInput]:
        return list(self.__d.values())
"""