import streamlit as st

st.markdown("<h1 style='text-align: center;transform: rotate(4deg); color: #FF5841;'>SQLaify</h1>",
            unsafe_allow_html=True)
# st.markdown("SQLaify")

styl = f"""
<style>
    .stTextInput {{
      position: fixed;
      bottom: 3rem;
    }}
</style>
"""
st.markdown(styl, unsafe_allow_html=True)
styl2 = f"""
<style>
    .stTextInput {{
      position: fixed;
      bottom: 5rem;
    }}
</style>
"""
st.markdown(styl, unsafe_allow_html=True)
txt = st.text_input(label=" ", placeholder='Write your question', )

st.code(txt)
