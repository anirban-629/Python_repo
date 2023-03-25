print("Case 1\n")
d2={"Anirban":"Meat","Sucho":"Pizza","Ritesh":"Fuchka"}
d3=d2
print(d3)
del d3["Anirban"]
print(d3)
print(d2)
# Here we are not making copy of d2 that why if we delete in d3 then d2 will also change

print("\nCase 2\n")
names_1={"Anirban":"Meat","Sucho":"Pizza","Ritesh":"Fuchka"}
names_2=names_1.copy()
print(names_2)
del names_2["Anirban"]
print(names_2)
print(names_1)
# Here that will not be changed as name_2 is just a copy of names_1