class Solution:
    def countDigit(n):
        if n==0:
            return 1
        cnt = 0
        while n > 0:
            cnt+=1
            n=n//10
        return cnt
# print(Solution.countDigit(234))
# print(Solution.countDigit(0))

