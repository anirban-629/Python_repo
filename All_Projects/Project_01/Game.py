import random

def game(a,b):
    # If two values are equal, declare a tie!
    if comp == you:
        print("Oopps..it's tie!!")

    # Check for all possibilities when computer chose s
    elif comp == 1:
        if you == 2:
            print("You lose!..Computer own")
        elif you == 3:
            print("You own..!!")

    # Check for all possibilities when computer chose w
    elif comp == 2:
        if you == 3:
            print("You lose!..Computer own")
        elif you == 1:
            print("You own..!!")

    # Check for all possibilities when computer chose g
    elif comp == 3:
        if you == 1:
            print("You own..!!")
        elif you == 2:
            print("You lose!..Computer own")

r=1
while r:
    print("\t\t\tWelcome to Snake Water Gun Game\n\n")
    a=input("Enter your name: ")
    b="Hello "+ a
    print(b)
    print("\nComputers Turn : Snake/Water/Gun")
    comp=random.randint(1,3)
    if comp==1:
        compu="Snake"
    elif comp==2:
        compu="Water"
    else:
        compu="Gun"
    print("Process Completed..")
    you=int(input("\nYours Turn : Snake(1)/Water(2)/Gun(3): "))
    print("Computer has Chosen",compu)
    if you==1:
        user="Snake"
    elif you==2:
        user="Water"
    elif you==3:
        user="Gun"
    else:
        user="Invalid!!!"
    print("You've Chosen ",user)
    game(comp,you)
    runornot=int(input("Do you want to play again(1 for Play again / 0 for Exit): "))
    if runornot==0:
        break
