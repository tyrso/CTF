from string import ascii_lowercase
from string import ascii_uppercase
import numpy
alphabetl = ascii_lowercase+''
alphabetu = ascii_uppercase+''
inp=open('test.txt','r')
inp_str=str(inp.read())
encode_str=''
for i in inp_str:
    if(i!=' ' and i!='\n'):
        encode_str+=i
inp.close()
inp=open('test.txt','w')
inp.write(encode_str)
inp.close()
print(len(encode_str))
sz = int(input("in how many word:"))
klen=6
key_num=0
cnt=[]
for i in range(klen):
    cnt.append({})
for i in range(len(encode_str)):
    if(len(encode_str)-i <= sz):
        break
    ch=''
    for j in range(sz):
        ch+=encode_str[i+j]
    if ch in cnt[key_num]:
        cnt[key_num][ch]=cnt[key_num][ch]+1
    else:
        cnt[key_num][ch]=1
    key_num=(key_num+1)%klen
sorted_dict_values=[]
for i in range(klen):
    sorted_dict_values.append(dict(sorted(cnt[i].items(), key=lambda item: item[1],reverse=True)) )
for i in range(klen):
    tmp = 0
    print('num ',i)
    for key in sorted_dict_values[i]:
        print(key,cnt[i][key])
        tmp+=1
        if(tmp == 5) :
            break
    print()
for i in range(klen):
    tmp = 0
    for key in sorted_dict_values[i]:
        #print(alphabetu[alphabetu.find(key)-alphabetu.find('E')],end='')
        tmp+=1
        if(tmp == 2) :
            #print()
            break
en_pass=str(input("encrypted password: "))
decode="FREKEYFRE"
for i in range(len(en_pass)):
    print(alphabetu[(alphabetu.find(en_pass[i])-alphabetu.find(decode[i%klen])+26)%26],end='')

    
# num0 :J=E   decode A = F
# num1 :V=E          A = R
# num2 :I=E          A = E        
# num3 :O=E          A = K
# num4 :I=E          A = E
# num5: C=E          A = Y
