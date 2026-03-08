class Solution:
    def factorial(self,n):
        if n ==1:
            return 1
        else:
            return n * self.factorial(n-1)

sol = Solution()
print(sol.factorial(3))