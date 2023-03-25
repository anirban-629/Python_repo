dictionary={
    "Anirban":"Mishra",
    "Sucho":"Das",
    "Sourin":"Ghosh",
    "Ritesh":"Saha"
}
print("Initial Dictionary is: ")
print(dictionary)

# .keys Functions
print("\n.keys Functions: ")
print(dictionary.keys())

# .values Functions
print("\n.values Functions: ")
print(dictionary.values())

# .items Functions
print("\n.items Functions: ")
print(dictionary.items())

# .update functions
print("\n.update Functions: ")
dictionary.update({"Arkhopravo":"Sarkar"})
print(dictionary)

# .get Functions
print("\n.get Functions: ")
print(dictionary.get("Anirban"))

# That's how a programme works properly

# Differnce between .get method and normal using [" "] is that while using .get
# if the string is not present it'll execute and say "None" but in case of others it'll throw error

print("\n",dictionary.get("asdg"))
# print(dictionary["asfsg"]) #-->This will throw error