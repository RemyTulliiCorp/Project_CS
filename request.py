# importing the libraries requests for HTTP requests to web servers
# importing APIKeys to easily use the API we want by only modifying the name 
import requests
from api_keys import all_keys
import streamlit as st

# defining a function that will allow to search the API using a query (future ingredients) put in by the user and the parameters containing the information to access the API
def search_recipes(your_ingredients, cuisine_type = None, max_time = None, excluded_ingredients = None, max_calories = None):
  api_key1 = all_keys['remy_key_spoonacular'] #setting the api keys to the respective keys as we created more than one account to have more free queries
  api_key2 = all_keys['matteo_key_edamam']
  api_id2 = all_keys['matteo_id_edamam']
  api_url1 = "https://api.spoonacular.com/recipes/extract" #setting the two api urls for the query to go through to the api
  api_url2 = 'https://api.edamam.com/search'

  #defining the parameters of the query which will be sent to the API in order to get a valid response with data
  params = { 
    'q': your_ingredients,
    'app_id' : api_id2,
    'app_key' : api_key2
  }
  
  if cuisine_type: # == if the cuisine box is checked
    params['cuisineType'] = cuisine_type # new query parameter added
  
  if max_time: # == if the max_time is selected
    params['time'] = f'1-{max_time}' # new query parameter added
  if excluded_ingredients:
    params['excluded'] = excluded_ingredients.split(',')

  if max_calories:
    params['calories'] = max_calories

  response = requests.get(api_url2, params = params) #making the request to the API using the parameters defined above and the second api url link
  
# checking if the request was successfull
# return a json of the API response was successful, otherwise return None to avoid errors
  if response.status_code == 200:
    return response.json()
  else:
    return None
  





