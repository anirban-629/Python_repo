line=input("Enter: ")
if("click here" in line):
    spam= True
elif("Subscribe this" in line):
    spam=True
elif("Make money" in line):
    spam=True
else:
    spam=False

if(spam):
    print("This is a spam")
else:
    print("This is not a spam")