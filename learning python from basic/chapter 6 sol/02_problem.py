marks1=int(input("Enter marks 1: "))
marks2=int(input("Enter marks 2: "))
marks3=int(input("Enter marks 3: "))

if(marks1<33 or marks2 <33 or marks3<33):
    print("fail")
elif((marks1+marks2+marks3)/3<=40):
    print("fail")
else:
    print("Congratulation you are pass.")