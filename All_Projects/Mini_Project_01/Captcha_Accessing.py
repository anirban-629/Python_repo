import random

def captcha():
    c_list1=['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z'
            'A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    c1=str(random.randint(1,9))
    c2=str(random.randint(1,9))
    c3=str(random.randint(1,9))
    c4=random.choice(c_list1)
    c5=random.choice(c_list1)
    c6=random.choice(c_list1)
    c_list2=[c1,c2,c3,c4,c5,c6]
    choice1=random.choice(c_list2)
    choice2=random.choice(c_list2)
    choice3=random.choice(c_list2)
    choice4=random.choice(c_list2)
    choice5=random.choice(c_list2)
    choice6=random.choice(c_list2)
    captcha=choice1+choice2+choice3+choice4+choice5+choice6
    return captcha

password ="Anirban"
cap=captcha()
print("Captcha:",cap)
pasw=input("Enter your Password: ")
captcha=input("Enter the Captcha: ")

if captcha==cap:
    if pasw==password:
        print("Captcha Correct")
        print("Passsword Correct")
        print("-------------------------------------")
        with open("Captcha.txt", "r") as file:
            content=file.read()
            print(content)
        print("-------------------------------------")
    else:
        print("Wrong Password")
else:
    print("Wrong captcha")

