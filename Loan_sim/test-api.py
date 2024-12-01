import requests

add_URL = "https://math-app-cxahara9dxdpcahb.canadacentral-01.azurewebsites.net/add"
sub_URL = "https://math-app-cxahara9dxdpcahb.canadacentral-01.azurewebsites.net/subtract"
a = 5
b = 6
data = {"a":a, "b":b }
response = requests.post(add_URL, json=data)

print(f"the answer is {response.json()['result']}")