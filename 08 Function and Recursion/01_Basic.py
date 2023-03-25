def factorial(a):
    fac=1
    for i in range(1,a+1):
        fac=fac*i
    return fac

x=int(input("Enter a Number: "))
print(f"Factorial {x} =",factorial(x))