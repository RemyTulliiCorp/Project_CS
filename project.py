import streamlit as st
import requests
from request import search_recipes
# Title
st.title('Kitchen:red[Alchemy]')
# User input for ingredients 
your_ingredients = st.text_input('Enter the ingredients you have in your fridge, separated by a coma', placeholder="Chicken, rice")
# button to select the cuisine type: chinese, italian, etc.
cuisine_type = st.selectbox('Choose a cuisine type (optional)', ('', 'American', 'Asian', 'British', 'Caribbean', 'Central Europe', 'Chinese', 'Eastern Europe', 'French', 'Indian', 'Italian', 'Japanese', 'Kosher', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Nordic', 'South American', 'South East Asian'), index=0)
# filter the maximum time period
max_time = st.selectbox('Maximum total time in minutes', ('', '15', '30', '45'), index=0, key='time')
# filter the excluded ingredients
excluded_ingredients = st.text_input('Enter the ingredients you want to exclude')
# button to lauch the search
output_recipes = st.button('Find Recipes')


if output_recipes: # == if you press on the button
    data = search_recipes(your_ingredients, cuisine_type if cuisine_type else None, max_time if max_time else None, excluded_ingredients) # calls the function
    if data: # == if a recipe exists
        meals = data.get("hits") #hits comes before recipe
        for meal in meals:
            recipe = meal.get("recipe") #recipe comes before image and label
            st.image(recipe['image']) # put an image of the recipe
            st.subheader(recipe['label']) # give the name of the recipe
            st.write(f' Total calories: {round(recipe["calories"])}') # calories 
            if recipe['totalTime']>0:
                st.write(f" {round(recipe['totalTime'])} minutes") # cooking time
            for ingredient in recipe['ingredientLines']:# write the necessary ingredients for each recipe
                st.write(f'{ingredient}')
            url_recipe = recipe['url']
            st.markdown(f"[Recipe Instructions]({url_recipe})") # give a link to the instruction to cook the recipe
            st.markdown('<hr>', unsafe_allow_html = True) # line separator between each recipe
    else:
        st.write('No recipe was found :hankey:')




