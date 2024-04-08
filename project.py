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
        meals = data.get("hits")
        for meal in meals:
            recipe = meal.get("recipe")
            st.image(recipe['image']) # put an image of the recipe
            st.subheader(recipe['label']) # give the name of the recipe
            
    else:
        st.write('No recipe was found :hankey:')


        

        



