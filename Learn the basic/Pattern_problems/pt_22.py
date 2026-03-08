n=4
size=n*2
# for i in range(1,n*2):
#     for j in range(1,n*2):
#         if(i==1 or j==1 or i==(n*2-1) or j==(n*2-1)):
#             print("4 ",end="")
#         elif(i==2 or j==2 or i==(n*2-2) or j==(n*2-2)):
#             print("3 ",end="")
#         elif(i==3 or j==3 or i==(n*2-3) or j==(n*2-3)):
#             print("2 ",end="")
#         elif(i==4 or j==4):
#             print("1 ", end="") 
#         else:
#             print("  ",end="")
#     print(end="\n")
for i in range(1,n*2):
    for j in range(1,n*2):
        for k in range(1,n+1):
            if(i==k or j==k or i==(n*2-k) or j==(n*2-k)):
                print(n-k+1," ",end="")
                break 
    print(end="\n")


# for i in range(1,size):
#     for j in range(1,size):
#         for k in range(1,n+1):
#             if i==k or j==k or i==(size-k) or j==(size-k):
#                 print(n-k+1," ",end="")
#                 break
#     print(end="\n")