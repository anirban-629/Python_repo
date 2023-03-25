def add(a,b):
    return a+b
def show(string):
    return f"Your string -->> {string}"

# Here name will be the main function
print("""__name__""","-->>",__name__)

# if we dont use the main function then when we'll import this file
# then all the codes will be also executed on that file that's why
# we have to use this

if __name__ == '__main__':
    print(add(10,20))
    print(show("Anirban"))
