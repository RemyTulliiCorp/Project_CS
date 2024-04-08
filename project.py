import streamlit as st
import requests
from request import search_recipes
# Title
st.title(':violet[KitchenAlchemy]')
# User input for ingredients 
your_ingredients = st.text_input('Enter the ingredients you have in your fridge, separated by a coma')
# button to lauch the search
output_recipes = st.button('Find Recipes')

if output_recipes == True:
    recipes = search_recipes(your_ingredients)
    for i in recipes:
                st.subheader(i['recipe']['label'])
                st.image(i['recipe']['image'])



