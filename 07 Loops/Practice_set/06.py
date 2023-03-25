num=int(input("Enter the nth element: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"Factorial of {num} is {factorial}")
# f string is used to get that function in print statement
