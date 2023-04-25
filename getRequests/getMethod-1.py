import requests


response = requests.get("https://reqres.in/api/users/2")
data = response.json()


print(data['data']['first_name'])
print(data.get('data').get('first_name'))
