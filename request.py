#importing the libraries requests for HTTP requests to web servers
#importing APIKeys to easily use the API we want by only modifying the name 
import requests
import APIKeys 
from APIkeys import remy_key_spoonacular, remy_key_edamam, matteo_key_spoonacular, matteo_key_edamam, remy_id_edamam, matteo_id_edamam


#defining a function that will allow to search the API using a query (future ingredients) put in by the user and the parameters containing the information to access the API
#checking if the request was successfull
#return a json of the API response
def search_recipes(query):
  api_key1 = remy_key_spoonacular
  api_key2 = remy_key_edamam
  api_id2 = remy_id_edamam
  api_url1 = "https://api.spoonacular.com/recipes/findByIngredients"
  api_url2 = 'https://api.edamam.com/search'
  params = { 
    'q': query,
    'app_id' : api_id2,
    'app_key' : api_key2
  }
  response = requests.get(api_url2, params = params)
  if response.status_code == 200:
    return response.json()
  else:
    return None
  
  search_recipes(pasta)
  


