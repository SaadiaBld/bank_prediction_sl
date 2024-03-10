from fastapi import FastAPI
from pydantic import BaseModel
import model_utils


app = FastAPI()
model = model_utils.load_model()


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
    category: int


@app.post("/predict")
def prediction_root(feature_input: FeaturesInput):
    F1 = feature_input.Term
    F2 = feature_input.FranchiseCode
    F3 = feature_input.UrbanRural
    F4 = feature_input.RevLineCr
    F5 = feature_input.LowDoc
    F6 = feature_input.GrAppv
    F7 = feature_input.SBA_Appv
    F8 = feature_input.NAICS_digit

    pred = model_utils.prediction(model, [[F1, F2, F3, F4, F5, F6, F7, F8]])

    return PredictionOutput(category=pred)
