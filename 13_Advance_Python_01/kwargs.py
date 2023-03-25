def printDetails(**kwargs):
    print(len(kwargs))
    for key,value in kwargs.items():
        print(key,value)


def main():
    details={
        'A':10,
        'B':20,
        'D':30,
        'E':40,
        'F':50,
    }
    printDetails(**details)

if __name__=='__main__':
    main()