n=4
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(0,i):
        print(chr(65+j),end="")
    for k in range(63+i,64,-1):
        print(chr(k),end="")
    print(end="\n")