n=5
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end="")
    print(" "*((n-i)-1)*2,end="")
    for k in range(i,0,-1):
        print(k,end="")
    print(end="\n")