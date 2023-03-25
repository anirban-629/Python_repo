def msum(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return a+msum(a-1)


n=int(input("Enter the last number: "))
print(f"Sum of n Natural Numbers are: {msum(n)}")
