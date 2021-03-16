#random password generator
import string,random
def password(length,num,strength):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    letter=upper+lower
    dig=string.digits
    punct=string.punctuation
    pwd=''
    if strength =='weak':
        if num:
            length-=2
            for i in range(0,2):
                pwd+=random.choice(dig)

        for i in range(length):
            pwd+=random.choice(lower)
    elif strength=='strong':
        if num:
            length-=2
            for i in range(length):
                pwd+=random.choice(dig)
        for i in range(length):
            pwd+=random.choice(letter)
    elif strength=='very strong':
        ran=random.randint(2,4)
        if num:
            length-=ran
            for i in range(ran):
                pwd+=random.choice(punct)
            for i in range(length):
                pwd+=random.choice(letter)
    pwd=list(pwd)
    random.shuffle(pwd)
    return ''.join(pwd)
length=int(input('enter the length of the password:'))
strength=input('enter the strength of your password')
num=True
print(password(length,num,strength))

