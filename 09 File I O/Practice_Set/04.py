with open("04_Article.txt") as file:
    data=file.read()
a=data.replace("donkey","######")
with open("04_Article.txt","w") as f:
    f.write(a)
print("Go and Check the txt file...!")

