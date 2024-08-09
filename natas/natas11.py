import base64
a = str(input())
b = str(input())
b2 = base64.b64decode(b)
print(len(a))
print(b2)