import streamlit as st
from openai import OpenAI
from utility import PromptCreation

st.markdown("<h1 style='text-align: center;transform: rotate(4deg); color: #FF5841;'>SQLaify</h1>",
            unsafe_allow_html=True)
# st.markdown("SQLaify")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
styl = " <style> .stTextInput {{ position: fixed; top: 10rem; }} </style> "

st.markdown(styl, unsafe_allow_html=True)
txt = st.text_input(label=" ", placeholder='Write your question', )

styl2 = "<style> .stCode {{ position: fixed; top: 25rem;}} </style>"
st.markdown(styl2, unsafe_allow_html=True)

if txt:
    response = PromptCreation.generic_prompt(client, txt)
    st.code(response, language='sql', line_numbers=False)
