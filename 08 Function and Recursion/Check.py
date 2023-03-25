def average(f):
    s=0
    for n in range(len(f)):
        s=s+f[n]
    av=s/len(f)
    return av


m=int(input("Enter how many marks you want to add: "))
marks=[]
for i in range(m):
    a=[int(input(f"Enter marks {i+1}: "))]
    marks.append(a)
# print(marks)
b=average(marks)
print("Average of Your Marks:",b)



# list=[100,200,300,400,500]5
# for i in range(5):
#     print(list[i])
