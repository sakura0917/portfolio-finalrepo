'''4. Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend.'''

import requests
url = "https://www.python.org/"
try:
    response = requests.get(url, timeout=5) 
    if response.status_code == 200:
        print(f"Your website {url} is working!")
    else:
        print(f"Your website {url} did not return a 200 status code. Instead it sent {response.status_code} ")
except requests.exceptions.RequestException as e:
    print(f"Could not connect to {url}. Error: {e}")
