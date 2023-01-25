import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel
from Student import Student
import joblib
from fastapi import FastAPI

app = FastAPI(title='StudBud', version='1.0',
              description='The pivot every student deserves.')

#loading models
encoder  = joblib.load('../model/encoder.joblib')
clf = joblib.load('../model/lgb_model.joblib')
numerical_features = joblib.load('../model/numerical_features.joblib')
categorical_features = joblib.load('../model/categorical_features.joblib')

#root endpoint
@app.get('/')
@app.get('/home')
def read_home():

    return {'message': 'Welcome to StudBud'}


#endpoint for the placement prediction
@app.post("/predict")
def predict(data: Student):
    data = data.dict()

    df = pd.DataFrame.from_dict([data])
    
    features = np.concatenate((numerical_features,categorical_features))

    #prepare df for prediction
    df = df[features]

    #preprocess - OneHotEncoding for cat_cols
    df_cat = encoder.transform(df[categorical_features])


    #transform the df in the right format for prediction
    df_final = np.concatenate((df_cat, df[numerical_features].to_numpy()),axis=1)

    # Create prediction
    prediction = clf.predict(df_final)

    #map the pred to label
    prediction_label = ['Placed' if label == 0 else 'Not Placed' for label in prediction ]

    return {"prediction": prediction_label}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)