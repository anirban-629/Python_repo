print("Full marks is 300 and each subject 100 marks")
phy=int(input("Enter your marks in Physics: "))
chem=int(input("Enter your marks in Chemistry: "))
math=int(input("Enter your marks in Math: "))

tot=phy+chem+math

if(tot>=120 and phy>=33 and chem>=33 and math>=33):
    print("You're  Passed")
else:
    print("You,re Failed")
