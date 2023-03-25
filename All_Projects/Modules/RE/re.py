import re
mystr='''
Regular expressions (called REs, or regexes, or regex patterns) are essentially a tiny, highly specialized programming language embedded inside Python and made available through the re module. Using this little language, you specify the rules for the set of possible strings that you want to match; this set might contain English sentences, or e-mail addresses, or TeX commands, or anything you like. You can then ask questions such as “Does this string match the pattern?”, or “Is there a match for the pattern anywhere in this string?”. You can also use REs to modify a string or to split it apart in various ways.123213-494

Regular expression patterns are compiled into a series of bytecodes which are then executed by a matching engine written in C. For advanced use, it may be necessary to pay careful attention to how the engine will execute a given RE, and write the RE in a certain way in order to produce bytecode that runs faster. Optimization isnt covered in this document, because it requires that you have a good understanding of the matching engines internals.

The regular expression language is relatively small and restricted, so not all possible string processing tasks can be done using regular expressions. There are also tasks that can be done with regular expressions, but the expressions turn out to be very complicated. In these cases, you may be better off writing Python code to do the processing; while Python code will be slower than an elaborate regular expression, it will also probably be more understandable.
'''
# findall, search ,split, sub, finditer

# r -> print(r'\n') rawstring

# a=re.compile(r'internals')
# matches=a.finditer(mystr)
# for match in matches:
#     print(match)

# print(mystr[1058:1067])

# a=re.compile(r'.')
# . any character

# a=re.compile(r'^exp') 
# ^ means startswith
# a=re.compile(r'ble&')
# ^ means endsswith

# a=re.compile(r'a*i*')
# 0 a or i and more than 0 a or i
# a=re.compile(r'ai*')
# a and 0 i or  more than 0 i

a=re.compile(r'\d{6}-\d{3}')

matches=a.finditer(mystr)
for match in matches:
    print(match)

