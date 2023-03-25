list=["A","B","C","D"]

# i=1
# for item in list:
#     if i%2!=0:
#         print(f"Item {i} to buy: {item}")
#         i+=1

for index,item in enumerate(list):
    if index%2==0:
        print(f"Item {index} -> {item}")
