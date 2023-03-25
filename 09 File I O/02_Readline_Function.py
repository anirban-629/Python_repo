file=open("sample.txt")
# Read 1st line
alldata=file.readline()
print(alldata)
# Read 3rd line
alldata=file.readline()
print(alldata)
# Read 2nd line
alldata=file.readline()
print(alldata)
# This will print blank because no 4th line check sample.txt
alldata=file.readline()
print(alldata)
file.close()

# Here It'll print a blank space because in \
# file also next line mean /n that's why  it's printing a single blank line