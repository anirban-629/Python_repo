name=input("Enter your name: ")
date=input("Enter the date: ")
string='''
Dear <|NAME|>
You're selected!
<|DATE|>
'''
# Wrong Process
# string.replace("NAME",name)
# string.replace("DATE",date)
string=string.replace("<|NAME|>",name)
string=string.replace("<|DATE|>",date)

print(string)