import os
with open("11_renam.txt") as file1:
    data=file1.read()
with open("11_renamed_by_Python.txt","w") as file2:
    file2.write(data)

os.remove("11_renam.txt")
print("Process Completed..!")