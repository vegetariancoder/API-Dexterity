import requests

# this is the base url
base_api_url = "https://jsonplaceholder.typicode.com"

# this is the additional 'endpoint' url
source_api_url = "/todos/"

# fetching the response using the GET method
response = requests.get(base_api_url+source_api_url)

print(response.text)
print(response.status_code)
print(response.elapsed.total_seconds())
print(response.headers['Content-Type'])
