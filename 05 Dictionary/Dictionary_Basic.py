dict={
"Tiger":"Lion",
"Fat":"Mat",
"Dog":"Fog"
}
print(dict)
print(type(dict))
print(dict["Tiger"])
print(dict["Fat"])

# Dictionary is mutable
dict["Tiger"]=[12,324,456]
print(dict["Tiger"])

dict["Tiger"]=["Lion"]
print(dict["Tiger"])
