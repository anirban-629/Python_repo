list=["anirban","sucho","sourin","ritesh","arka","angira","supriti","ankit","disha"]
name=input("Enter a name to check list: ")
name=name.lower()
if name in list:
    print("Yes, entered name is present in list")
else:
    print("Entered name is not present in list")