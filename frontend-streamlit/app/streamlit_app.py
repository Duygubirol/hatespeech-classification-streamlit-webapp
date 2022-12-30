import json

import requests
import streamlit as st
from PIL import Image

st.title("Hate Speech Detection Web-app")

# image = Image.open("./app/images/profile-pictures-slack.jpeg")
# st.image(image, caption="Hello, it's me")

sentence = st.text_input(
    "Please enter the sentence you want to detect hate speech:")
# converting the inputs into a json format
inputs = {"input_text": sentence}

# when users click on this button, the web-app will call the API
if st.button("Show result"):
    #json.dump() will produce a .json file
    result = requests.post(url="http://172.17.0.1:8000/predict",
                           data=json.dumps(inputs))

    st.subheader(f"This speech is classified as {result.text}")
