import base64
encoded_str = str(input())
decoded_bytes = base64.b64decode(encoded_str)
decoded_str = decoded_bytes.decode('utf-8')  

print("decode_str is:", '\n',decoded_str)