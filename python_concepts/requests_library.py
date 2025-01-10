# REQUESTS LIBRARY

# https://requests.readthedocs.io/en/latest/

# The easiest requests library known to man.

import requests


def basic_get_request():
    # this is even overkill, but let's include error handling
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

    # check if successful
    if response.status_code == 200:
        print("Success")
        print(response.json())
    else:
        print(f"FAILED: {response.status_code}") 

basic_get_request()
