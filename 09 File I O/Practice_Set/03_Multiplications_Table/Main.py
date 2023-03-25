a=int(input("Enter a Number: "))
with open("Table.txt","w") as f1:
    for i in range(10):
        f1.write(f"{a}X{(i+1)}={a*(i+1)}\n")
print("Go and Check the file Table..!!")