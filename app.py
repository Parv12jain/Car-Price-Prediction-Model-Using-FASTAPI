#import fastapi
#model creation for fastapi
#loading pickle file
#making predict endpoint

from fastapi import FastAPI
import pickle
import pydantic
from pydantic import BaseModel
from typing import Literal
import pandas as pd
from fastapi.responses import JSONResponse
app = FastAPI(title="This is our first ML API project")


#Validation class
class PricePredict(BaseModel):
    name:str
    year:int
    km_driven:int
    fuel:Literal[0,1,2,3]
    seller_type:Literal[0,1,2]
    transmission:Literal[0,1]
    owner:Literal[0,1,2,3,4]
    # mileage(km/ltr/kg):float
    engine:float
    max_power:float
    seats:float

#Predicts post endpoint
@app.post('/predict')
def predict(data:PricePredict):
    input_df = pd.DataFrame([{
        'year':data.year,
        'km_driven':data.km_driven,
        'fuel':data.fuel,
        'seller_type':data.seller_type,
        'transmission':data.transmission,
        'owner':data.owner,
        # 'mileage(km/ltr/kg)':data.mileage(km/ltr/kg),
        'engine':data.engine,
        # 'max_power':data.max_power,
        'seats':data.seats
    }])
    prediction = model.predict(input_df)[0]
    return JSONResponse(content={"Prediction":prediction})




with open('model.pkl','rb') as fs:
    model = pickle.load(fs)

@app.get('/')
def greet():
    return {"This is Project Home page go on docs for prediction"}