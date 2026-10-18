# def star_print(n):
#     for i in range(n):
#         print("*"*(n-i))


def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)


n=int(input("Enter number: "))
pattern(n)
