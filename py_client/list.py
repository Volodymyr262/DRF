import requests

auth_endpoint = 'http://localhost:8000/api/auth/'
password = input('password:')
auth_response = requests.post(auth_endpoint,
                             json={
                               'username': 'volodymyr',
                               'password': password
                             })
print(auth_response.json())


endpoint = 'http://localhost:8000/api/products/'

get_response = requests.get(endpoint)
print(get_response.json())