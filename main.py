import random;

char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+=-[]|:;<>?/.,~`'


len=int(input("Enter Desired Password Length: "))

password = ''.join(random.sample(char,len))

if len <=0:
    print("Please ensure length is greater than 1")
else:
    password=''.join(random.sample(char,len))
    print(password)
