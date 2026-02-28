n=5
for i in range(0,n):
    print(" "*(n-i),end="")
    print("*"*(((i)*2)-1),end="")
    print(end="\n")

for i in range(0,n):
    print(" "*i,end="")
    print("*"*(((n-i)*2)-1),end="")
    print(end="\n")