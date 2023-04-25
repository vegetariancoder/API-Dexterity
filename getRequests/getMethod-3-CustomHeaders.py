import requests
import logging

Authorization = {
    "token": "sdfdsfgsrgs",
    "user-agent": "learning"
}

logging.basicConfig(level=logging.INFO)
logging.info(f"custom token is {Authorization}")
response = requests.get("https://learning.free.beeceptor.com", headers=Authorization, )
response_code = response.headers
logging.info(f"The response code is {response_code}")
