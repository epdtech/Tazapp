import streamlit as st
import google.generativeai as genai



api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)


model = genai.GenerativeModel('gemini-1.5-flash')





col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Taz")

with col2:
    st.image("images/taz.jpg")

st.title(" ")

persona = """
        You are Taz AI bot. You help people answer questions about your self (i.e Taz)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Taz: 
        I Am a pomchow dog
        Taz is an Educator/Youtuber/Entrepreneur in the field of bones and Eating sticks..
        He runs one of the largest YouTube channels in the field of bones and Eating sticks.
        Taz was born in 2020
        I went to doggy bone high where I studied chewing bones and Eating sticks.
        Taz obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
         He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Taz worked as a design engineer, evaluating 
        and developing rapid prototypes of Doggy Bones.

        Taz's Youtube Channel: https://www.youtube.com/channel/big doggy bone
        Taz's Email: contact@BigDoggybone.com 

        """

st.title("Taz's AI Bott")

user_question = st.text_input("Ask anything about me")
if st.button("ASK ME", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)


user_question = st.text_input("Ask anything else")

if st.button("ASK ANYTHING", use_container_width=400):
    prompt = user_question
    response = model.generate_content(prompt)
    st.write(response.text)
    # print(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Taz Channel")
    st.subheader("watch my video")

with col2:
    #st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")
    video_file =open("images/TazSpinn - Trim.mp4", 'rb')
    st.video(video_file)

st.title(" ")

st.title("My Setup")
#st.image("images/setup.jpg")

# st.subheader(" ")
st.write(" ")
st.slider("Programming", 0,100,50)
st.slider("Teaching", 0,100,70)
st.slider("Robotics", 0,100,20)
# st.slider("barking skills", 0,100,100)

# st.file_uploader("Upload a file")
st.write(" ")
st.title("Gallery")

col1,col2,col3 = st.columns(3)

with col1:
    st.image("images/taz1rot.jpg")
    st.image("images/taz2rot.jpg")
    st.image("images/tazlion.jpg")

with col2:
    st.image("images/tsz55.jpg")
    st.image("images/taz6cr.jpg")
    st.image("images/taz7cr.jpg")

st.write("CONTACT")
st.title("For any inquiries, please contac me at:")
st.write("taz@taz.com")
