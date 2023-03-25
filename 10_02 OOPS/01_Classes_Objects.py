'''
Class         : Template
Objects       : Instance of class (Content)
DRY Principle : Don't Repeat Yourself
'''

class student:
    pass

anirban=student()
sucho=student()

anirban.name="ANIRBAN MISHRA"
anirban.roll=2
anirban.yr="2nd year"

sucho.name="SUCHORITA DAS"
sucho.roll=1
sucho.yr="1st year"

print(anirban,sucho) #-> Address

print(anirban.name)
print(sucho.name)