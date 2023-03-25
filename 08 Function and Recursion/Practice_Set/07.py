def nwstr(string,word):
    str=string.replace(word,"*")
    return str.strip()

n=input("Enter a Sentence: ")
a="           "+n
print(a,"-> ""Now the Process is going on""")
b=input("Enter the word you want to Remove: ")
print("Sending the sentence to Remove the First word and the blank spaces")
print(nwstr(a,b))