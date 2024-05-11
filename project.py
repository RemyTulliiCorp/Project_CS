import streamlit as st
import requests
from request import search_recipes
import pandas as pd
import mathplotlib.pyplot

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
#slider to choose the calories
max_calories = st.slider('Maximum number of calories', 100, 5000, 2500, 100)
# sorting option
sort_option = st.selectbox('Sort recipes by',options=('', 'Calories', 'Cooking Time', 'Number of ingredients'),index=0)
# button to lauch the search
output_recipes = st.button('Find Recipes')


if output_recipes: # == if you press on the button
    data = search_recipes(your_ingredients, cuisine_type if cuisine_type else None, max_time if max_time else None, excluded_ingredients, max_calories)

    if data: # == if a recipe exists
        meals = data.get("hits")
        if sort_option == 'Calories':
            sorted_meals = sorted(meals, key=lambda x: x['recipe']['calories']) # sorting condition one
        elif sort_option == 'Cooking Time':
            sorted_meals = sorted(meals, key=lambda x: x['recipe'].get('totalTime', 0))   # second sorting condition
        else:
            sorted_meals = meals

        for meal in sorted_meals: # loop that get the recipes that meet the specified conditions
            recipe = meal.get("recipe") #recipe comes before image and label
            st.image(recipe['image']) # put an image of the recipe
            st.subheader(recipe['label']) # give the name of the recipe
            servings = recipe['yield']
            st.write(f" For {servings} persons")
            st.write(f" Calories per serving: {round(recipe['calories']/servings)}") # calories 
            if recipe['totalTime'] > 0:
                st.write(f" {round(recipe['totalTime'])} minutes") # cooking time
            for diet in recipe['dietLabels']:
                st.write(diet)
            nutrients = meal['recipe']['totalNutrients'] # extraction of the nutritional data
            protein = nutrients.get('PROCNT', {}).get('quantity', 0)/servings
            fats = nutrients.get('FAT', {}).get('quantity', 0)/servings
            carbs = nutrients.get('CHOCDF', {}).get('quantity', 0)/servings

            #Create a DataFrame to hold the nutritional data
            chart_data = pd.DataFrame({
                'Nutrients': ['Proteins', 'Lipids', 'Carbs'], 
                'Macronutrients (g)': [protein, fats, carbs],
                })
            chart_data.set_index('Nutrients', inplace=True)
            with st.expander("Show Nutrients"):
                st.bar_chart(chart_data, y=['Macronutrients (g)'])

            for ingredient in recipe['ingredientLines']:# write the necessary ingredients for each recipe
                st.write(f'{ingredient}')
            url_recipe = recipe['url']
            st.markdown(f"[Recipe Instructions]({url_recipe})") # give a link to the instruction to cook the recipe
            st.markdown('<hr>', unsafe_allow_html = True) # line separator between each recipe
    
    else:
        st.write('No recipe was found :hankey:')
    



