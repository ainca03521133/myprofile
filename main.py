import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width= 400)

with col2:
    st.title("蕭政緯")
    content ="""東海大學畢業，畢業後於家中以及協助事業，後來認為東海大學
    後來認為東海大學畢業，畢業後於家中以及協助事業，後來認為
    後來認為東海大學畢業，畢業後於家中以及協助事業，後來認為
    後來認為東海大學畢業，畢業後於家中以及協助事業，後來認為
    後來認為東海大學畢業，畢業後於家中以及協助事業，後來認為
    """
    st.info(content)