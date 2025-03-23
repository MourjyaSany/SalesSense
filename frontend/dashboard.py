import streamlit as st
import requests

st.title("Lead Scoring Dashboard")

name = st.text_input("Enter Lead Name")
email = st.text_input("Enter Lead Email")

if st.button("Get Lead Score"):
    response = requests.post("http://127.0.0.1:5000/score", json={"name": name, "email": email})
    score = response.json().get("lead_score")
    st.write(f"Lead Score: {score}")
