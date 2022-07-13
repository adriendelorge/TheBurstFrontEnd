import time
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from PIL import Image
import webbrowser
# from TheBurst import cities_data, main_file, map, transports, utils


# https://www.youtube.com/watch?v=nSw96qUbK9o (for integrate de data)

def main_page():
    st.sidebar.markdown("COMPANY INFO")

    image = Image.open('image/logorecortado.png')

    st.image(image, width=700)


    st.title('WELCOME')

    st.write('What is The Burst?')


    st.markdown(
    """
    An optimization model for decentralization of corporate headquarters to rural areas and small cities

    ### What do we do?
    - Optimize your data
    - Create a model based on your business/life preferences
    - Provide you with cities top recommendations, where you have the most chances of success

    ### Benefits

    👉 CHOOSE --> The best place for your headquarters

    👉 GAIN --> Quality of life

    👉 SUPPORT --> Regional Economies""")

    url = 'http://localhost:8501/page1'

    if st.button('Take me to the app 💡'):
        webbrowser.open(url, new=2)

main_page()
