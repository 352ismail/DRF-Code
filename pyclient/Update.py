import requests

endpoint = "http://localhost:8000/api/products/50/update"

data={"title" : "Gifting Items" ,
       "price":"2090",
       "content":"these Items are out of stock"}

response = requests.put(endpoint,json=data)
if response.status_code == 200:
    print(response.json())
    #print(response.status_code)
else:
    print(response)
    print(response.status_code) 