import time

#1-> time.time()
time_for_Execution=time.time()
print(time_for_Execution) # In mili seconds

#2-> time.ctime()
seconds=time.time()
i=time.ctime(seconds)
print(i)

#3-> gmtime()
i1=time.gmtime() # GM-> Greenich mean time
print(i1)

#4-> localtime()
i2=time.localtime() #Local-> Local indian Time
print(i2)


