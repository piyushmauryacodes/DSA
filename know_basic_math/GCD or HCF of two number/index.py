n1=48
n2=64
limit = min(n1,n2)
hcf =1
if n1==n2:
    print(n1)
for i in range(2,limit):
    if(n1%i==0 and n2%i==0):
        hcf=i
print(hcf)
