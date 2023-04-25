import requests
import logging

# set logger
logging.basicConfig(level=logging.INFO)


# way of sending data in the url
logging.info("sending data using url only")
response = requests.get("https://learning.free.beeceptor.com?key1=value1&key2=value2")
logging.info(response.status_code)

# way of sending data using params
parameters = {
    'name': 'sahil',
    'age': 23
}
logging.info("sending data using url params")
response = requests.get("https://learning.free.beeceptor.com",params=parameters)
logging.info(response.status_code)