import streamlit as st
import requests

st.title("📊 SalesSense - AI CRM Dashboard")

name = st.text_input("Enter Lead Name")
email = st.text_input("Enter Lead Email")

# Initialize score to None
score = None  

if st.button("Get Lead Score"):
    response = requests.post("http://127.0.0.1:5000/score", json={"lead_data": name})
    
    if response.status_code == 200:
        score = response.json().get("lead_score")
        st.session_state["score"] = score  # Store in session
        st.write(f"⭐ Lead Score: {score}")
    else:
        st.write("❌ Error getting lead score")

# Ensure score is retrieved before allowing lead addition
if "score" in st.session_state:
    if st.button("Add Lead"):
        response = requests.post("http://127.0.0.1:5000/add_lead", 
                                 json={"name": name, "email": email, "score": st.session_state["score"]})
        st.write(response.json().get("message", "Error adding lead"))
else:
    st.write("❌ Please generate a Lead Score first!")
