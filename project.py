import streamlit as st
import requests
from request import search_recipes
st.title('Kitchenalchemy')
st.write("testt")
ingredients = search_recipes('pastas')
st.write(ingredients)