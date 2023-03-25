import random

def greet(name):
    print("WELCOME ",name.upper())

def chose():
    words=["function","string","list","tuple","dictionary","files","input","output","oops",
           "loops","recursion","indentation","python","high","level","language","programming"]
    pick=random.choice(words)
    return pick

def jumbling(word):
    jumbled= "".join(random.sample(word, len(word)))
    return jumbled

def play():
    score = 0
    turn = 1
    while(1):
        qstn = chose()
        jmbld = jumbling(qstn)
        print("Guess The word -->", jmbld)
        ans1 = input("Your answer: ")
        ans=ans1.lower()
        if ans == qstn:
            score = score + 1
            print("Hurrah!! You Guessed it...\nYour Score: ", score)
        else:
            print("Oops Wrong answer..! Better luck next time\nScore= ",score)
        play_or_exit=int(input("Press 1 to continue and 0 to exit.. : "))
        if play_or_exit == 0:
            print("Bye",name.capitalize(),"Your Score is: ",score)
            break


print('\t-:   THE GUESSING GAME    :-\n\n')
name=input("Enter your name: " )
greet(name)
play()
