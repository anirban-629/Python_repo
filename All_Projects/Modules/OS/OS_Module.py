import os

# Current working Directory..
# print(os.getcwd())

# Change Current Working Directory...
# Here we've changed the current working directory
# os.chdir("D://")
# print(os.getcwd())

# List in directory
# print(os.listdir("D:\Code editors\Python_Language\Py_in_one"))

# Making Directory
# os.mkdir("OS1")
# Making Sub Directories
# os.makedirs("OS2/OS3")

# Renaming
# os.rename("OS2","OS22")

# Getting environment variable
# print(os.environ.get("Path"))

# Joining two paths
# print(os.path.join("D://","/Name.txt"))

# Checking path
# print(os.path.exists("D://Code Editors"))
# print(os.path.exists("D:// Editors"))

# Isdir/isfile...
print(os.path.isdir("D://Code Editors"))
print(os.path.isdir("D://Code Editors/Python_Language/Py_in_one/01_Basics/02_comments_escape_sequences.py"))
print(os.path.isfile("D://Code Editors/Python_Language/Py_in_one/01_Basics/02_comments_escape_sequences.py"))