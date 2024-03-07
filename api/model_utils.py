from joblib import load
import pandas as pd

def load_model(path='modelcatb.pkl'):
    model = load(path)
    return model

def prediction(model, data):
    df = pd.DataFrame(data, columns=['Term', 'FranchiseCode', 'UrbanRural', 'RevLineCr', 'LowDoc', 'GrAppv', 'SBA_Appv', 'NAICS_digit'])
    prediction = model.predict(df)
    return prediction[0]


# La routes GET : récupérer tous les items ou un item spécifique par son ID
# La route POST : créer un nouvel item
# La route PUT : mettre à jour un item existant par son ID
# La route DELETE : supprimer un item existant par son ID
