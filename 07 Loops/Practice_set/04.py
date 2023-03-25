num=int(input("Enter a number to check if prime or not: "))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
if prime:
    print("Number is Prime")
else:
    print("Number is not Prime''")