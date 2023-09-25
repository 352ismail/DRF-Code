import requests



product_id = input("Product Id: ")

try: 
    productId = int(product_id)
except: 
    print(f'{product_id} is not a valid productId')

if productId:
    endpoint = f"http://127.0.0.1:8000/api/products/{productId}/delete"

    response = requests.delete(endpoint )
    if response.status_code == 200:
        print(response.json())
        #print(response.status_code)
        
    elif response.status_code == 500:
        print("Internal server responded with 500 Error")
    else:
        print(response.json())
        print(response.status_code) 
