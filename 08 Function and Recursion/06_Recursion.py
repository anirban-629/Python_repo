def factorial_Recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_Recursion(n-1)

def factorial_Normal(i):
    b=1
    for i in range(i):
        b=b*(i+1)
    return b

a=int(input("Enter a number: "))
print(f"Factorial {a}=",factorial_Recursion(a))
print(f"Factorial {a}=",factorial_Normal(a))
