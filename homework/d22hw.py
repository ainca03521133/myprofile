import streamlit as st
import pandas as pd

df = pd.read_csv("homework/data.csv")

st.set_page_config(layout="wide")

st.title("The Best Company")
content = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
"""
st.write(content)

st.subheader("Our Team")

col1 , col2, col3 = st.columns([1, 1, 1])

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"].title())
        st.image("homework/images/"+ row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"].title())
        st.image("homework/images/"+ row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"].title())
        st.image("homework/images/"+ row["image"])