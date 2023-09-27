import requests
from  getpass import getpass

#get token 
auth_endpoint = "http://127.0.0.1:8000/api/auth/"


username = input("Enter your username: ")
password = getpass(prompt="Enter your password: ")
#your credentials
data ={
    "username":username,
    "password":password
}
auth_response = requests.post(auth_endpoint, json=data)
if auth_response.status_code == 200:

    token = auth_response.json()["token"]
    print(token)

    headers = {"Authorization":f"Bearer {token}"}
        # Send the token in request headers 
    endpoint = "http://127.0.0.1:8000/api/products/"
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        print(response.json())
        #print(response.status_code)
    else:
        print(response.json())
        print(response.status_code) 
    print(auth_response.json())
    #print(response.status_code)
else:
    print(auth_response.json())
    print(auth_response.status_code) 



