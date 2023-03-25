list=[1,2,3,4,5]

# in keyword
print(5 in list)
print(10 in list)

# not in keyword
print(10 not in list)
print(5 not in list)

print("Enter a number if it's in a list: ")
n=input()

if n in list:
    print("Yes this is in list")
else:
    print("No not in List")