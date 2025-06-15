import streamlit as st
from chatbot import load_health_data, get_response

st.set_page_config(page_title="AI Health Chatbot")
st.title("🩺 AI Health Chatbot")
st.write("Ask me anything about your health symptoms!")

user_input = st.text_input("You:", "")

if user_input:
    data = load_health_data()
    response = get_response(user_input, data)
    st.write(f"💬 Bot: {response}")
