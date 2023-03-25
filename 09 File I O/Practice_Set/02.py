def game():
    import random
    a=random.randint(1,100)
    return a

score=game()
print("Score is:",score)
with open("02_score.txt") as file:
    data=int(file.read())

if score>data:
    with open("02_score.txt","w") as file:
        file.write(str(score))


