# file=open("sample.txt","r")
# if we do'nt specify the mode of the file in code
# then it'll automatically take it as read mode
file=open("sample.txt")
alldata=file.read()

# alldata=file.read(10)
# If we do thge over then only 10 words will be printed

print(alldata)
file.close()