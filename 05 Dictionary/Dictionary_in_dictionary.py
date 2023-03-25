dictionary={
    "Ram":1,
    "Sam":2,
    "Anirban":
        {"Jodu":100,
         "Modu":200
}
}
print(dictionary)
print("\nDictionary in Dictionary: ")
print(dictionary["Anirban"])
print("Printing values of dictionary in dictionary: ")
print("\n",dictionary["Anirban"]["Jodu"])
print("\n",dictionary["Anirban"]["Modu"])
