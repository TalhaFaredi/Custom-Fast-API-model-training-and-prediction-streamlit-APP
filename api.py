from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

clf = joblib.load('model.joblib')

class_names = ['setosa', 'versicolor', 'virginica']

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()

@app.post('/predict')
def predict(data: IrisData):
    prediction_data = [
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]

    prediction = clf.predict([prediction_data])

    return {
        'prediction': class_names[int(prediction[0])]
    }
