import streamlit as st
import requests
from request import search_recipes
# Title
st.title(':violet[KitchenAlchemy]')
# User input for ingredients 
your_ingredients = st.text_input('Enter the ingredients you have in your fridge, separated by a coma')
# button to lauch the search
output_recipes = st.button('Find Recipes')

if output_recipes: # == if you press on the button
    recipes = search_recipes(your_ingredients) 
    for i in recipes:
                st.subheader(i['recipe']['label'], divider = 'blue')
                st.image(i['recipe']['image'])
                for ingredient in i['recipe']['ingredientLines']:
                    st.write(f"- {ingredient}")


