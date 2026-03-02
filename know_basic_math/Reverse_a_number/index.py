class Solution:
    def reverseNumber(n):
        num=0
        if n > 0:
            while n > 0:
                rem=n%10
                num=num * 10 + rem
                n=n//10
            return num
        else:
            n = n * (-1)
            while n > 0:
                rem=n%10
                num=num * 10 + rem
                n=n//10
            return num * (-1)
            
print(Solution.reverseNumber(1534236469))