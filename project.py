import streamlit as st
import requests
from request import search_recipes
# Title
st.title(':violet[KitchenAlchemy]')
# User input for ingredients 
your_ingredients = st.text_input('Enter the ingredients you have in your fridge, separated by a coma')
# button to lauch the search
output_recipes = st.button('Find Recipes')
# button to select the cuisine type: chinese, italian, etc.
cuisine_type = st.selectbox('Choose a cuisine type', ('', 'American', 'Asian', 'British', 'Caribbean', 'Central Europe', 'Chinese', 'Eastern Europe', 'French', 'Indian', 'Italian', 'Japanese', 'Kosher', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Nordic', 'South American', 'South East Asian'), index=0)

if output_recipes: # == if you press on the button
    data = search_recipes(your_ingredients, cuisine_type if cuisine_type else None)
    if data: # == if a recipe exists
        meals = data.get("hits") #hits comes before recipe
        for meal in meals:
            recipe = meal.get("recipe") #recipe comes before image and label
            st.image(recipe['image']) # put an image of the recipe
            st.subheader(recipe['label']) # give the name of the recipe
            st.write(recipe['calories'])
            st.write(recipe['totalTime'])
    else:
        st.write('No recipe was found :hankey:')




