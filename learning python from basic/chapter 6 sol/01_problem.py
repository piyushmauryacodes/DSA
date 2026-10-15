# s=set()


# num=int(input("Enter number: "))
# s.add(num)

# num=int(input("Enter number: "))
# s.add(num)

# num=int(input("Enter number: "))
# s.add(num)

# num=int(input("Enter number: "))
# s.add(num)

# print(max(s))


a1=int(input("Enter number 1: "))
a2=int(input("Enter number 2: "))
a3=int(input("Enter number 3: "))
a4=int(input("Enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print(f"Greatest number is {a1}")
elif(a2>a3 and a2>a4):
    print(f"Greatest number is {a2}")
elif(a3>a4):
    print(f"Greatest number is {a3}")
else:
    print(f"Greatest number is {a4}")

