from fastapi import FastAPI,HTTPException,Body
import json
# creating instance of (or object)
app = FastAPI()


# HTTPS method 1 - GET is used to fetch data or read data

@app.get('/greet')
def greet():

    return "Hello World"

@app.get('/about')
def about():
    return "this is the about page"


@app.get('/feedback')
def feedback():
    return " this is the feedback page"

def load_data():
    with open("data.json", 'r') as fs:
        data = json.load(fs)
    return data

def save_data(data):
    with open("data.json", 'w') as fs:
        json.dump(data, fs)


# endpoint -> data.json complete data dekhta hai

@app.get('/view')
def view():
    return load_data()

# endpoint -> ek specific id ka data view krna hai
@app.get("/view/{patient_id}") # jab bhi specific id view krege toh sath me id bhi lihni padegi jese for eg mene patirnt id likhi ha
def view_id(patient_id): # yaha call krdo
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return "not found"
   
# Creating new patient by using POST
# import HTTPException , Body
@app.post('/create/{patient_id}')
def create(patient_id:str,patient:dict=Body(...)):
    data = load_data()
    if patient_id in data:
        raise HTTPException(status_code=400,detail="patient already exit")
    
    data[patient_id] = patient
    save_data(data)

# Endpoint for updating patient
@app.put('/edit/{patient_id}')
def edit(patient_id:str, update_data:dict=Body(...)):
    data = load_data()
    # check if patient already exit or not
    if patient_id not in data:
        raise HTTPException(status_code=400,detail="patient not found")
    
    # existing patient data
    patient_data = data[patient_id]

    # update only provided data
    for key,value in update_data.items():
        patient_data[key] = value

    # save data
    save_data(data)


# endpoint for deleting record
@app.delete('/remove/{patient_id}')
def remove(patient_id:str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=400,detail="patient not found")
    del data[patient_id]
    save_data(data)

