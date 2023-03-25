with open("06_07_log_file.txt") as f:
    data=f.read().lower()

if "python" in data:
    print("Python is Present")
else:
    print("Python is Absent")
