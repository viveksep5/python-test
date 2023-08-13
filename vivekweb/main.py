import streamlit as st
import pandas as pd
     
st.write("""
# My first app
Hello *world!*
""")
     
df = pd.read_csv("my_data.csv")
st.line_chart(df)
st.image("kids.jpg")
st.video("mainframe.mp4")
st.button('Click me')
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
st.camera_input("Take a picture")
st.color_picker('red')

