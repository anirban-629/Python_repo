c=1
i=1
with open("06_07_log_file.txt") as f:
    while c:
        c=f.readline()
        if "python" in c.lower():
            print(f"Python found in line no {i}")
        i+=1


