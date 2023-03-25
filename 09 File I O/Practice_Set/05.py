with open("05_poem_2.txt") as file:
    data=file.read()
data=data.replace("little","#*@!&^%$")
data=data.replace("I","#*@!&^%$")
data=data.replace("twinkle","#*@!&^%$")
data=data.replace("star","#*@!&^%$")

with open("05_poem_2.txt","w") as f:
    f.write(data)
print("Process completed! check..")