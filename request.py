import requests
import APIKeys 

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
  
  
