import requests

# for i in range(50,100,2):
endpoint = "http://127.0.0.1:8000/api/products/"

headers = { "Authorization": "Bearer f55b0d7c7f4c335aa4b157d60c38838bc0146a84"}


data = {
        "title":f"Gifting Items",
        "content":"Packings of gifts for all type of itmes",
        "price": 1200
}
response = requests.post(endpoint, json=data, headers=headers)
if response.status_code == 200:
    print(response.json())
    #print(response.status_code)
else:
    print(response.json())
    
    print(response.status_code) 