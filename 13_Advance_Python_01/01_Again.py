a=input("Enter Number: ")
print("Enter e to exit")
while(1):
    if a=='e':
        break
    try:
        a=int(a)
        if a>=8:
            print('Greater tha equals to 8')
    except Exception as e:
        # print(e)
        print("Error")
print("Thank you..")
