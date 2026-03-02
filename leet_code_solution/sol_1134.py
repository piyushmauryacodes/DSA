class Solution:
    def isArmstrong(n):
        temp=n
        s=str(n)
        size=len(s)
        sum=0
        for i in range(1,size+1):
            rem=n%10
            sum= sum + (rem**size)
            n=n//10
        if temp==sum:
            return temp==sum
        else:
            return temp==sum

print(Solution.isArmstrong(3711))
