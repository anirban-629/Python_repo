name="Anirban is my name"
print("Length of the string is: ",len(name))

# len() THis is used to get the length of the string

print(name[0:7])
# array indexing starts from 0
# here 0 is including and 7 is excluding that means if we give 6 here it will not take
# 0 is the starting point

# Advance:
print(name[0:7:2])
# print you will understand

print(name[0:7:3])
print(name[::4]) #By default it's start with 0
print(name[0::2])
print(name[-4:])
print(name[2:7])

# TO MAKE A STRING IN REVERSE ORDER:

print(name[::-1 ])