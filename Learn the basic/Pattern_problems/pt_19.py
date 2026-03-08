n=5
for i in range(0,n):
    print("*"*(n-i),end="")
    print("  "*i,end="")
    print("*"*(n-i),end="")
    print(end="\n")
for i in range(0,n):
    print("*"*(i+1),end="")
    print("  "*(n-i-1),end="")
    print("*"*(i+1),end="")
    print(end="\n")