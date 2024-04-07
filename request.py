import requests
import APIKeys 
from APIkeys import remy_key_spoonacular

def search_recipes(query):
  api_key = 
  api_id = 
  api_url = 'https://api.edamam.com/search'
  parameters { 
    'q': query,
    'api_id' : api_id,
    'api_key' : api_key
  }
  response = requests.get(api_url, params = params)
  if response.status_code == 200:
    return response.json()
  else:
    return None
  
  
spoonacular_key = remy_key_spoonacular
url = 'https://api.spoonacular.com/recipes/findByIngredients'
params = {
    'apiKey': spoonacular_key,
    'query': 'pasta'
}

response = requests.get(url, params=params)
data = response.json()



