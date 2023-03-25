class Student:
    # Class variable
    no_of_students=100

anirban=Student()
sucho=Student()

# Instance variable
anirban.name="Anirban"
anirban.roll=1
anirban.section="A"
print(anirban.__dict__)

sucho.name="Sucho"
sucho.roll=2
sucho.section="A"
print(sucho.__dict__)

print(f"Before change no of students: {Student.no_of_students}")
Student.no_of_students=101
print(f"After change no of students: {Student.no_of_students}")

anirban.no_of_students=102
print(anirban.__dict__)
# Here in this case the class variable will not be
# changed here a new instance variable will be created