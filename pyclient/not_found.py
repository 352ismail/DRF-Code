import requests

endpoint = "http://127.0.0.1:8000/api/products/209090/"


response = requests.get(endpoint)
if response.status_code == 200:
    print(response.json())
    #print(response.status_code)
else:
    print(response.json())
    print(response.status_code) 