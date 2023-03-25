import random
print("Welcome to Rock Paper Scissor game\n")

def compChoice():
    com=["r","p","s"]
    choice=random.choice(com)
    return choice
# print(compChoice())
comp=compChoice()

def userChoice():
    choice=input("Rock/Paper/Scissor: ").lower()
    if choice=="rock" or choice=="paper" or choice=="scissor":
        return choice
    else:
        print("Invalid..")
user=userChoice()
# print(user)

# ds=defaultScore
ds=0
def game(comp,user,score):
    if comp=="r" and user=="rock":
        print(f"Tie..\nscore:{score}\n")
    if comp=="r" and user=="paper":
        print(f"Computer own..\nscore:{score}\n")
    if comp=="r" and user=="scissosr":
        score-=1
        print(f"Computer own..\nscore:{score}\n")
    if comp=="p" and user=="rock":
        score+=1
        print(f"You won..\nscore:{score}\n")
    if comp=="p" and user=="paper":
        print(f"Tie..\nscore:{score}\n")
    if comp=="p" and user=="scissor":
        score+=1
        print(f"You won..\nscore:{score}\n")
    if comp=="s" and user=="rock":
        score+=1
        print(f"You won..\nscore:{score}\n")
    if comp=="s" and user=="paper":
        score-=1
        print(f"Computer own..\nscore:{score}\n")
    if comp=="s" and user=="scissor":
        print(f"Tie..\nscore:{score}\n")

    return score

while(1):
    score=game(comp,user,ds)
    # a=int(input("Press any number to coninue or 0 to exit: "))
    # if(a==0):
    #     print("Your final score is: ",score)
    #     exit()


# not successfull
