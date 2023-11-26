import streamlit as st
import requests
from pydantic import BaseModel

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

sepal_length = st.number_input('Enter sepal length')
sepal_width = st.number_input('Enter sepal width')
petal_length = st.number_input('Enter petal length')
petal_width = st.number_input('Enter petal width')

if st.button('Get prediction'):
    data = IrisData(
        sepal_length=sepal_length,
        sepal_width=sepal_width,
        petal_length=petal_length,
        petal_width=petal_width
    )

    response = requests.post('http://localhost:8000/predict', json=data.dict())

    prediction = response.json()['prediction']

    st.write(f'The predicted species is: {prediction}')
