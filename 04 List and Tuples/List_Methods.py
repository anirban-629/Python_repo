#Sorting
list1=[234,346,87,436,87,2,42,576,0,46,987]
list1.sort()
print("Sorted list: ",list1)

# Reverse
list2=[123,45,56,89,43,7676,3,57,0]
list2.reverse()
print("\nReversed list before soritng: ",list2)
list2.sort()
print("Now sorted list: ",list2)
list2.reverse()
print("Reversed list after soritng: ",list2)

# Append
list3=[213,45,4567,78,32,678]
list3.append(21)
print("\nAppend 21...at the end: ",list3)

# Insert
list4=[1,2,3,4,5,6]
list4.insert(3,8)
print("\nAfter the particular index like here after index 3, 8 will be added: ",list4)

# Pop
list5=[12,3,445,6,7,8,967,7]
list5.pop(4)
print("\nHere at this list pop 4 means after index 4 will be deleted: ",list5)

# Remove
list6=[234,45,56,678,870]
list6.remove(234)
print("\nParticular mentioned will be deleted here: ",list6)

# Extend
list7=[21,312,435,456,678987,87]
list7.extend([123,324,43,65])
print(list7)