def sum_of_n(n):
    if (n==1):
        return 1
    else:
        n+=sum_of_n(n-1)
        return n


n=int(input("Enter number: "))
print(sum_of_n(n))
