import requests

response = requests.get("http://127.0.0.1:5000/get_status", auth=('droneport', 'password'))

if response.status_code == 200:
    print(response.json())
else:
    print("Error: ", response.status_code)