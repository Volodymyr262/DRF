import requests

endpoint = 'http://localhost:8000/api/'

get_response = requests.get(endpoint, json={"product_id": 1})
print(get_response.json())