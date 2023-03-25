def great(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c

    else:
        if b>c:
            return b
        else:
            return c

a=int(input("Enter Number 1: "))
b=int(input("Enter Number 2: "))
c=int(input("Enter Number 3: "))

print("The greatest Number is:",great(a,b,c))