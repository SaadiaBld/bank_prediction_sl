import requests


for i in range(50):
    feature_input = {
        "Term": float(i),
        "FranchiseCode": 1.0,
        "UrbanRural": 1.0,
        "RevLineCr": "Y",
        "LowDoc": "N",
        "GrAppv": 1,
        "SBA_Appv": 1,
        "NAICS_digit": 1,
    }
    r = requests.get("http://0.0.0.0:8001/predict", json=feature_input)
    print(r.content)
