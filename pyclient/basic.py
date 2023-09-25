import requests

endpoint = "http://127.0.0.1:8000/api/"

queryParams = {"Product_Id":123 , "Name":"Product Number 1"}
data = {"Messsage":"Hello World!" , "Response": {"Stauts":"Success"}}

response = requests.post(endpoint ,json={"title" : "Hello World" ,
                                         "price":"290",
                                         "content":"Helllo to the world"})
if response.status_code == 200:
    print(response.json())
    #print(response.status_code)
else:
    print(response.json())
    print(response.status_code) 
