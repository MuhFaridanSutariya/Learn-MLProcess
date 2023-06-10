from fastapi import FastAPI
from fastapi import Request

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
async def predict(data: Request):

    # load request 
    data = await data.json()

    sepal_length = data['sepal_length']
    sepal_width = data['sepal_width']
    petal_length = data['petal_length']
    petal_width = data['petal_width']

    model = load_model()
    input_data = [sepal_length, sepal_width, petal_length, petal_width]  

    try:
        prediction = model.predict([input_data])
        result = prediction[0]
        response = {
            "status": 200,
            "input": input_data,
            "message": result
        }
    except Exception as e:
        response = {
            "status": 204,
            "message": str(e)
        }

    return response
