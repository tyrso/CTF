#I write this program by myself. Sing here: 游承熹
#Email Address: neil93.9.14@gmail.com
#Anything special? 你的程式有什麼比較特別的地方?
#I provide additional functions: None
from string import ascii_lowercase
from string import ascii_uppercase
vis=[0]*26
alphabetl = ascii_lowercase+''
alphabetu = ascii_uppercase+''
def letter_to_idxl(ch):
    return alphabetl.find(ch)
def letter_to_idxu(ch):
    return alphabetu.find(ch)
def continue_or_not():
    con = ''
    while(1):
        print('do you want to continue?input y for yes and input n for not ')
        con = str(input())
        if(con!='n' and con!='y') :
            print('input error,please input again')
        else:
            break
    if(con=='n'):
        return 0
    else:
        return 1
def remove_duplicate(s):
    pwd=''
    for ch in s:
        idx=alphabetl.find(ch)
        if(vis[idx] == 0) :
            pwd=pwd+ch
        vis[idx]=1
    return pwd
def form_key(pwd):
    key=pwd
    for i in range(letter_to_idxl(pwd[-1]),26):
        if(vis[i] == 0):
            key=key+alphabetl[i]
    key = key + ' '
    for i in range( 0, letter_to_idxu(pwd[-1]) ):
        if vis[i] == 0 :
            key = key + alphabetl[i]
    print(key)
    return key

def encrypt_message(message,key):
    cipherText=''
    for ch in message:
        cipherText+=key[letter_to_idxl(ch)]
    return cipherText
def decrypt_message(cipherText,key):
    message=''
    for ch in cipherText:
        if alphabetl[alphabetl.find(ch)] == ch:
            message=message+alphabetl[(letter_to_idxl(ch)+13)%26]
        elif alphabetu[alphabetu.find(ch)] == ch:
            message=message+alphabetu[(letter_to_idxu(ch)+13)%26]
        else :
            message=message+ch
    return message
def get_key():
    print('please input the password')
    s=str(input())
    pwd = remove_duplicate(s)
    key = form_key(pwd)
    return key
while 1:
    key=13
    print('please input a message')
    message=str(input())
    #cipherText=encrypt_message(message,key)
    #print('the encrypted Text is '+cipherText)
    ans=decrypt_message(message,key)
    print('the decrypted message is '+'\n'+ans)
    if(continue_or_not()==0):
        break




    
