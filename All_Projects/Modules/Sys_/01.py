import sys
print("sys.platform -> ",sys.platform)
# print("sys.copyright -> \n\n",sys.copyright)
print("sys.version -> ",sys.version)
sys.stdout.write("sys.stdout.write\n")
# sys.stderr.write("sys.stderr.write") -> color - red
# sys.stderr.write("\nsys.stderr.write\n")

a="anirban"
b=1231
print(sys.getsizeof(b))
print(sys.getsizeof(a))

print(sys.argv)