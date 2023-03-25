marks=int(input("Enter Marks: "))
if (marks>=90 or marks==100):
    print("Your Grade is: O")
elif(marks>=80 or marks<90):
    print("Your Grade is: E")
elif(marks>=70 or marks<80):
    print("Your Grade is: A")
elif(marks>=60 or marks<70):
    print("Your Grade is: B")
elif(marks>=50 or marks<60):
    print("Your Grade is: C")
elif(marks>=40 or marks<50):
    print("Your Grade is: D")
elif(marks>=0 or marks<40):
    print("Your Grade is: F")
else:
    print("Invalid!!")