with open("chck1.txt") as file1:
    data1 = file1.read()
with open("chck2.txt") as file2:
    data2 = file2.read()

if data1==data2:
    print("These two files are same to same")
else:
    print("These files are not same")
