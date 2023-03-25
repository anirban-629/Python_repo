import time
initial1=time.time()
print(initial1)
i1=0
while i1<500:
    i1=i1+1
    print(i1)
print(f"While loop execution time -> {time.time()-initial1}")

initial2=time.time()
i2=0
for i in range(500):
    print(i2)
    i2=i2+1
print(f"For loop execution time -> {time.time()-initial2}")

