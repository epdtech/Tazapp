# 1. Add the streamlit library to the project.
import streamlit as st
# to test
# streamlit run taz_website.py

import google.generativeai as genai
# genai.configure(api_key=os.environ["API_KEY"])

genai.configure(api_key="AIzaSyCSlkKuF8BFF82FuHUBUnz5MZ6xTO4lS3M")

# api_key = st.secrets=["GOOGLE_API_KEY"]
# genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)


col1, col2 = st.columns(2)
with col1:
    st.subheader("Hi :wave:")
    st.title("I am Taz")

with col2:
    st.image("images/taz.jpg")

st.title(" ")
st.title("Taz's Ai Butt")

user_question = st.text_input("Ask anything about me")

if st.button("ASK", use_container_width=400):
    prompt = user_question
    response = model.generate_content(prompt)
    st.write(response.text)
    # print(response.text)

st.title(" ")
