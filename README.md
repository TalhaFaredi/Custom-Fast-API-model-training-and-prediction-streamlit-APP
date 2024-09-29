
```markdown
# Iris Species Prediction Web Application

This project implements a simple web application that predicts the species of an Iris flower based on user input features. The application uses a **Decision Tree Classifier** trained on the Iris dataset from Scikit-learn. It also demonstrates the use of **FastAPI** for serving the model as a REST API and **Streamlit** for building a web interface.

## Table of Contents
- [Introduction](#introduction)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [Running the Web App](#running-the-web-app)
- [Model](#model)
- [How It Works](#how-it-works)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Introduction

This application takes input parameters (sepal length, sepal width, petal length, petal width) from the user and predicts the species of the Iris flower (`setosa`, `versicolor`, or `virginica`) using a trained **Decision Tree Classifier** model. The model is served via **FastAPI**, and the prediction results are displayed in a **Streamlit** web interface.

## Architecture

The application consists of three components:
1. **Machine Learning Model**: A Decision Tree Classifier trained on the Iris dataset.
2. **FastAPI Server**: A REST API to serve the trained model.
3. **Streamlit App**: A web interface to input flower features and display the predicted species.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/iris-prediction-app.git
   cd iris-prediction-app
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` should include the following:
   - `fastapi`
   - `pydantic`
   - `scikit-learn`
   - `joblib`
   - `uvicorn`
   - `streamlit`
   - `requests`

4. **Train the model and save it:**
   Before running the app, the model needs to be trained and saved.
   ```bash
   python train_model.py
   ```

## Usage

### Running the API

1. **Start the FastAPI server:**
   Run the FastAPI server locally using `uvicorn`.
   ```bash
   uvicorn app:app --reload
   ```

   This will launch the API on `http://localhost:8000`.

2. **API Endpoints:**
   - `/predict`: Accepts POST requests with the Iris flower features and returns the predicted species.

### Running the Web App

1. **Start the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

2. **Using the Web Interface:**
   - Enter the **sepal length**, **sepal width**, **petal length**, and **petal width** values in the provided input fields.
   - Click the "Get prediction" button to see the predicted Iris species.

3. **Example Prediction:**
   After entering the flower features and submitting, you will get a result like:
   ```
   The predicted species is: setosa
   ```

## Model

The model used in this project is a **Decision Tree Classifier** from the Scikit-learn library. It is trained on the famous **Iris dataset**, which contains 150 records of iris flowers with 4 features each:
- Sepal length
- Sepal width
- Petal length
- Petal width

The model is saved using **joblib** as `model.joblib` for future predictions.

## How It Works

1. **Training the Model:**
   - The model is trained on the Iris dataset using a **Decision Tree Classifier**.
   - It is saved to disk as `model.joblib`.

2. **API for Prediction:**
   - A **FastAPI** server exposes an endpoint `/predict` that accepts a POST request containing the input flower features and returns the predicted species.
   - The model is loaded from `model.joblib`, and predictions are made on the provided data.

3. **Streamlit Frontend:**
   - The frontend is built using **Streamlit**. Users can input flower measurements via a web form.
   - Upon submission, a request is sent to the FastAPI server, and the predicted species is displayed in the app.

## Future Enhancements

- **Expand the model**: Use a more complex model (e.g., Random Forest or SVM) to improve accuracy.
- **Enhance the UI**: Improve the Streamlit interface with better styling and visualization.
- **Add Validation**: Implement input validation in both the frontend and the backend.
- **Deploy the API**: Deploy the FastAPI server to the cloud (AWS, Heroku) for real-world usage.

## License

This project is licensed under the MIT License.
```

### Additional Files:

1. **`app.py`** (Streamlit web app):
    This file contains the frontend code where users input flower features and submit the data for prediction.
  
2. **`app.py`** (FastAPI app):
    This file contains the backend FastAPI application which processes the input data and returns predictions.

3. **`train_model.py`**:
    This file is responsible for training the model using Scikit-learn’s Decision Tree Classifier and saving it as `model.joblib`.

Make sure to organize your project structure properly with the necessary files.
