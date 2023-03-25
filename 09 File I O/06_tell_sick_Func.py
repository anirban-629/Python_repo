with open("func.txt") as f:
    # print(f.tell())
    print(f.readline())
    print(f.seek(10))
    print(f.readline())
    print(f.tell())
    print(f.readline())
    # print(f.tell())

"""
f.tell says the character number at the particular pointing position...
f.seek hold the starting position and execute that
"""
