"""
In this try except if suppose we are taking two integer inputs so if there one input is not integer
then it'll throw error and further the program also will be exited so for this we use this two
keywords to handle this error in this case it'll also throw the error but it'll throw as a string
and will not exit it'll run the next instruction
"""
a=input("Enter A: ")
b=input("Enter B: ")
try:
    print(f"Addition-> {int(a)+int(b)}")
except Exception as e:
    print(e)

print("This line will execute now after using this or "
      "not if any error became at the previous")

