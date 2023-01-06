import json
from datetime import datetime

import requests
import streamlit as st
from PIL import Image

st.title("Stack UnderFlow")

image = Image.open("./app/images/elon.webp")
st.image(
    image,
    caption=
    "Elon Musk, who took over Twitter in October, has described himself as a “free speech absolutist.” \n Credit...Carina Johansen/NTB, via Reuters"
)

txt = st.subheader(
    "Hate Speech’s Rise on Twitter Is Unprecedented, Researchers Find")

txt = st.markdown("\n By Sheera Frenkel and Kate Conger. @nytimes \n")
txt = st.markdown(
    " Before Elon Musk bought Twitter, slurs against Black Americans showed up on the social media service an average of 1,282 times a day. \
    \n After the billionaire became Twitter’s owner, they jumped to 3,876 times a day. \n Slurs against gay men appeared on Twitter 2,506 times a day on average before Mr. Musk took over. Afterward, their use rose to 3,964 times a day."
)

txt = st.subheader('Comment Session')

sentence = st.text_input("Post your opinion about the post here.")
# converting the inputs into a json format
inputs = {"input_text": sentence}


def output_message(result: str) -> str:
    """ convert prediction result into meaningful messages.
    """
    if result == '"not_hate"':
        return 'Your comment has been posted.'
    if result == '"offensive"':
        return 'Your comment seems to be offensive. Please edit it.'
    if result == '"implicit_hate"':
        return 'Your comment seems to contain implicit hateful content. It will be manually reviewed by our team.'
    if result == '"explicit_hate"':
        return 'Your comment seems to contain explicit hateful content. It was reported to the concerned parties.'


# when users click on this button, the web-app will call the API
if st.button("Post"):
    #json.dump() will produce a .json file
    # 172.17.0.1 is the address within the Docker
    result = requests.post(url="http://172.17.0.1:8000/predict",
                           data=json.dumps(inputs))

    # this code is to test front end separately on localhost
    # result = requests.post(url="http://0.0.0.0:8000/predict",
    #                        data=json.dumps(inputs))

    st.subheader(output_message(result.text))

    if result.text == '"not_hate"':
        txt = st.markdown(sentence)
        now = datetime.now()
        txt = st.markdown(now.strftime("%d/%m/%Y %H:%M:%S"))
