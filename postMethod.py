import requests

# this is the base url
base_api_url = "https://jsonplaceholder.typicode.com"

# this is the additional 'endpoint' url
source_api_url = "/todos/"

# constructing main url
main_url = base_api_url+source_api_url

# adding my own data
todo = {"userId": 47, "title": "learning-api", "completed": False}

response = requests.post(
    url=main_url,
    data=todo,
    timeout=2
)

print(response.json())
print(response.status_code)

print(response.text)


