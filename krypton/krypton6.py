#SINGOGODDESSTHEANGEROFACHILLESSONOFPELE
from string import ascii_lowercase
from string import ascii_uppercase
import numpy
alphabetl = ascii_lowercase+''
alphabetu = ascii_uppercase+''
alphabet= alphabetu+alphabetl
decode_inp=open("decode.txt",'r')
decode=decode_inp.read()
decode_inp.close()
en_key="PNUKLYLWRQKGKBE"
sz = len(decode)
for i in range(len(en_key)):
    print(alphabetu[(alphabetu.find(en_key[i])-alphabetu.find(decode[i])+26)%26],end='')