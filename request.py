# importing the libraries requests for HTTP requests to web servers
# importing APIKeys to easily use the API we want by only modifying the name 
import requests
from api_keys import all_keys
import streamlit as st
# defining a function that will allow to search the API using a query (future ingredients) put in by the user and the parameters containing the information to access the API
# checking if the request was successfull
# return a json of the API response
def search_recipes(your_ingredients, cuisine_type = None, max_time = None, excluded_ingredients = None, max_calories = None):
  api_key1 = all_keys['remy_key_spoonacular'] # change the name if limit exceeded
  api_key2 = all_keys['matteo_key_edamam'] # change the name if limit exceeded
  api_id2 = all_keys['matteo_id_edamam'] # change the name if limit exceeded
  api_url1 = "https://api.spoonacular.com/recipes/findByIngredients"
  api_url2 = 'https://api.edamam.com/search'
  params = { 
    'q': your_ingredients,
    'app_id' : api_id2,
    'app_key' : api_key2
  }
  
  if cuisine_type: # == if the cuisine box is checked
    params['cuisineType'] = cuisine_type # new query parameter added
  
  if max_time:
    params['time'] = max_time

  if excluded_ingredients:
    params['excluded'] = excluded_ingredients

  if max_calories:
    params['calories'] = f'0-{max_calories}'

  response = requests.get(api_url2, params = params)

  if response.status_code == 200:
    return response.json()
  else:
    return None
  





