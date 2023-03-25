def convrt(a):
    f=(a*1.8)+32
    return f

c=int(input("Enter Celsius: "))
print(f"{c} Degree Celsius = {convrt(c)} Degree Fahrenheit")