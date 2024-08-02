from string import ascii_lowercase
from string import ascii_uppercase
import numpy
alphabetl = ascii_lowercase+''
alphabetu = ascii_uppercase+''
cnt={}
inp=open('test.txt','w')
for i in inp:
    if i == ' ' or i == '\n':
        i = ''
encode_str=str(inp.read())
inp.close()
password=''
idx = 0
message=''
#sz = int(input("in how many word:"))
sz=0
for i in range(len(encode_str)):
    message=''
    ch=encode_str[i]
    if ch==' ' or ch=='\n':
        continue
    k=i
    while len(message)!=sz:
        ch=encode_str[k]
        if ch!=' ' and ch!='\n':
            message+=ch
        k+=1
        if(k == len(encode_str)):
            break
    if(k==len(encode_str)):
        break
    if message in cnt:
        cnt[message]=cnt[message]+1
    else:
        cnt[message]=1
sorted_dict_values = dict(sorted(cnt.items(), key=lambda item: item[1],reverse=True))
tmp = 0
for key in sorted_dict_values:
    #print(key,cnt[key])
    tmp+=1
    if(tmp == 10) :
        break
current_ans_e='JDSQVKIBGWYUNXMC'
current_ans_d='THEALWVONDPSRFUI'
password=str(input('encrypted:'))
for i in password:
    if current_ans_e.find(i)!=-1:
        print(current_ans_d[current_ans_e.find(i)],end='')
    elif alphabetu.find(i)!=-1:
        print(alphabetl[(alphabetu.find(i))],end='')
#LEVEL TWO PASSWORD ROTTEN
#level two password rotten