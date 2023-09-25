import requests

endpoint = "http://127.0.0.1:8000/api/products/50/"


response = requests.get(endpoint)
if response.status_code == 200:
    print(response.json())
    #print(response.status_code)
else:
    print(response)
    print(response.status_code) 
