def factorial(n):
    fact=n
    if(n==0 or n==1):
        fact=1
    else:
        fact*=factorial(n-1)
    return fact


n=int(input("Enter the number: "))

f=factorial(n)
print(f)