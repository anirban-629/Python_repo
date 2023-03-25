import random
print("\t\tWelcome to Number Guessing Game")
while(1):
    r=random.randint(1,100)
    i=None
    attempts=0
    while(i!=r):
        i=int(input("Enter a Number: "))
        attempts=attempts+1
        if i==r:
            print(f"You guessed the Number it {attempts} attempts")
        else:
            if i<r:
                print("Greater Number")
            else:
                print("Lesser Number")
    i1=int(input("Enter 1 to Continue\n0 to Exit\n--> "))
    if i1==0:
        exit()


