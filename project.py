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
    data = search_recipes(your_ingredients)
    if data: # == if a recipe exists
        for i in data:
            st.image(data.get("hits")[i]['recipe']['image']) # put an image of the recipe
            st.subheader(data.get("hits")[i]['recipe']['label']) # give the name of the recipe
            
    else:
        st.write('No recipe was found :hankey:')


        

        



