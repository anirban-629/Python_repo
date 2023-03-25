with open("1st.txt") as file1:
    data=file1.read()
with open("2nd.txt","w") as file2:
    file2.write(data)

print("Process Completed")