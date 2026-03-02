import math

n=13
if n<=0:
    print("Enter a Greater Number than zero.")
if n==1:
    print(n," is a prime Number")
for i in range(2,int(math.sqrt(n))+1):
    if n%i!=0:
        print(n," is a prime number")
        break
    else:
        print(n," is not prime number.")
        break
