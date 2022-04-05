from http import client
import streamlit as st
from sympy import re
import weaviate 
from weaviate.wcs import WCS

client = weaviate.Client("http://localhost:8080")

st.title('something')
choice = st.selectbox("Pick one",["Movie","TV Show"])

if choice== "Movie":
    name = st.text_input("Enter any concept related to movie")
    nearText = {
    "concepts": [name]
    }
    result = client.query.get(class_name='Movie', properties=["title"])\
    .with_limit(10)\
    .with_near_text(nearText)\
    .do()
    if st.button('Recommend'):
        for i in range (9):  
            st.write(result['data']['Get']['Movie'][i]['title']) 

if choice== "TV Show":
    name = st.text_input("Enter any concept related to TV Show")
    nearText = {
    "concepts": [name]
    }
    result = client.query.get(class_name='TvShow', properties=["title"])\
    .with_limit(6)\
    .with_near_text(nearText)\
    .do()
    if st.button('Recommend'):
        for i in range (6):  
            st.write("Name of TV Show : "+ result['data']['Get']['TvShow'][i]['title']) 
             
              


