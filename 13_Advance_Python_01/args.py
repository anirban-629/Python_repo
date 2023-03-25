def printDetails(*args):
    print(len(args))
    if(len(args)==3):
        print(f'Name: {args[0]}\nAge: {args[1]}\nSalary: {args[2]}')
    elif(len(args)==2):
        print(f'Name: {args[0]}\nAge: {args[1]}')
    else:
        print(f'Name: {args[0]}')


def main():
    # details=['Anirban']
    # details=['Anirban',20]
    details=['Anirban',20,10000]
    printDetails(*details)

if __name__=='__main__':
    main()