with open("01_poem.txt", "r") as file:
    data=file.read()
    print("Word found in position: ",data.find("twinkle"))