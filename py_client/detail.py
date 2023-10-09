import requests

endpoint = 'http://localhost:8000/api/products/4/'


get_response = requests.get(endpoint)
if get_response.status_code == 200:
    try:
        json_data = get_response.json()
        print(json_data)
    except ValueError:
        print("Response is not valid JSON.")
else:
    print(f"Request failed with status code {get_response.status_code}")
    print(get_response.text)