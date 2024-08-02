from string import ascii_lowercase
from string import ascii_uppercase
alphabetl = ascii_lowercase+''
alphabetu = ascii_uppercase+''
encode_str=str(input())
password=''
tries = int(26)
for t in range(13,14) :
    message=''
    for i in encode_str:
        ch = i
        fl = alphabetl.find(i)
        fr = alphabetu.find(i)
        if alphabetl[fl]==i :
            ch = alphabetl[(fl+t)%26] 
        elif alphabetu[fr] == i :
            ch = alphabetu[(fr+t)%26]
        message = message+ch
    print(message)
#LEVEL TWO PASSWORD ROTTEN
#level two password rotten