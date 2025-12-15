import streamlit as st 
import requests

API = 'http://127.0.0.1:8000/predict'



st.title("🚗 Car Price Prediction")
name = st.text_input("Car Name", placeholder="e.g. Maruti Swift Dzire")
year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, step=1)
km_driven = st.number_input("Kilometers Driven", min_value=0, step=1000)
fuel = st.selectbox("Fuel Type", [0,1,2,3])
seller_type = st.selectbox("Seller Type", [0,1,2])
transmission = st.selectbox("Transmission Type", [0,1])
owner = st.selectbox("Owner Type", [
    0,1,2,3,4
])
mileage = st.number_input("Mileage (km/ltr/kg)", min_value=0.0, step=0.1)
engine = st.number_input("Engine Size (CC)", min_value=500, step=50)
max_power = st.number_input("Max Power (bhp)", min_value=0.0, step=1.0)
seats = st.number_input("Number of Seats", min_value=1.0, max_value=20.0, step=1.0)

if st.button('Predict Now'):
    input_data = {
        'name':name,
        'year': year,
        'km_driven': km_driven,
        'fuel': fuel,
        'seller_type': seller_type,
        'transmission': transmission,
        'owner': owner,
        'mileage': mileage,
        'engine': engine,
        'max_power': max_power,
        'seats': seats
    }

    response = requests.post(API, json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"💰 Predicted Price: ₹{result['Prediction']}")
    else:
        st.error(f"{response.status_code} - {response.text}")