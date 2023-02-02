import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2,gap="large")

with col1:
    st.image("images/photo.jpg",width=500)

with col2:
    st.title("蕭政緯")
    st.header("自我介紹")
    introduce_chn ="""
    前三年因家庭有些特殊狀況，因此沒辦法進入職場，需要照顧家裡，而無法立即的投入職場，在家裡的事情解決後，也確實地
    有感受到一股對未來的徬徨，家裡的事暫時解決後，有在朋友推薦的教授底下作為助理開始工作，由於經由嘗試後，明確地感
    受到自己對文職工作的不喜歡，下定決心參與職訓局的計畫，很有幸的發現之前工作接觸到的人，有輕量化網站的需求，幫他
    們以wordpress建立網站，開始了嘗試性接案，並同時自我進修，一直擔心個人能力無法達到業內需求，直到人資朋友鼓勵，
    希望能用所學為貴司創造價值。

    目前會使用的技能為:
        -Java
        主要使用JDK 1.8進行開發，開發工具主要用Eclipse。

        -Spring框架
        Spring boot, Spring MVC, 和Spring REST,Spring cloud 都能靈活運用。配合需求開發出產品。

        -PHP
        能使用PHP寫出網頁後端平台配合基本Laravel框架。目前仍在學習中。
.
    """
    st.info(introduce_chn)
    
    
    st.header("Introduce")
    introduce_eng ="""
    In the past three years, due to some special circumstances in my family, I was unable to enter the workplace. I needed to take care of my family, so I was unable to immediately enter the workplace.
    Some felt hesitant about the future. After the family affairs were temporarily resolved, some started working as an assistant under a professor recommended by a friend. After trying, I clearly felt that
    Affected by my dislike of clerical work, I made up my mind to participate in the project of the Vocational Training Bureau. I was fortunate to find that the people I met in my previous work had a need for a lightweight website. Help him
    We set up a website with wordpress, began to accept cases tentatively, and at the same time self-educated.
    """
    st.info(introduce_eng)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)


col3, empty_col,col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv(".venv/data.csv",sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")