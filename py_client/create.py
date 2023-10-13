import requests

endpoint = 'http://localhost:8000/api/products/'

headers = {'Authorization': 'Bearer9668695d63d3a329123a2b53fb0064c28dad9ea4'}
data = {
    'title': 'This field is done',
    'price': '33.23'
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())