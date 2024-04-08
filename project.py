import streamlit as st
import requests
from request import search_recipes
st.title('Kitchenalchemy')
your_ingredients = st.text_input('Enter the ingredients you have in your fridge')

