from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# ==== Flow of code
# 1. Loading Model = [knn_model.pkl]
# 2. Get Input = [sepal_length, sepal_width, petal_length, petal_width]
# 3. Predict Model = expect 0 / 1 / 2

def load_model():
    try:
        path = open('model/knn_model.pkl', 'rb')
        classifier = pickle.load(path)
        return classifier
    except Exception as e:
        response = {
            "status":204,
            "message":str(e)
        }
        return response

@app.post("/predict")
async def predict(sepal_length: float, sepal_width: float, petal_length:float, petal_width: float):
    model = load_model()
    input = [[sepal_length, sepal_width, petal_length, petal_width]]

    try:
        prediction = model.predict(input)
        result = prediction[0]
        response = {
            "status":200,
            "input":[sepal_length, sepal_width, petal_length, petal_width],
            "message":result
        }
    except Exception as e:
        response = {
            "status": 204,
            "message": str(e)
        }
        
    return response