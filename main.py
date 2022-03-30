import streamlit as st
import cv2
import streamlit.components.v1 as components
from IPython import display


st.title("Interview Questions")
name = st.text_input("Enter your Name:")
email = st.text_input("Enter your Email:")
affiliation = st.text_input("Affiliation:")
area_of_intrest = st.text_input("Area of Intrest: ")
webpage = st.text_input("Home Page (eg : https://www.yourwebpage.com)")
code = st.text_input("Enter your 12-Digit Code:", max_chars=12)
camera_btn = st.button("Take photo")
if camera_btn:
  pass
    

if len(code) == 12:
    ur="https://scholar.google.co.in/citations?user="+code+"&hl=en"
    st.markdown(display.HTML(url=ur))



