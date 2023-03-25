# With Statement is used in python because
# if we use this then we don't need to close the file

with open("sample.txt","r") as file:
    a=file.read()
    print(a)        