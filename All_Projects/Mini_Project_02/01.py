a=int(input("Enter How many Students You want to add: "))
with open ("lib.txt",'a') as f:
    for i in range (a):
        n=input("Name: ")
        n.capitalize()
        r=input("Roll: ")
        final=n+"\t\t\t"+r
        f.write(final)
        f.write("\n")
