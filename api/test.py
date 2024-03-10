import model_utils

model = model_utils.load_model()

z = model_utils.prediction(model, [[1.0, 1.0, 1.0, "Y", "N", 10, 1, 1]])

print(f"-------------> {z}")
