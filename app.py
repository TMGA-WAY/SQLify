import streamlit as st

txt = st.text_input(label=" ", placeholder='Write your question')

st.code(txt)