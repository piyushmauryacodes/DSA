class Solution:
    def printNumbers(self,n):
        if n==0:
            return
        self.printNumbers(n-1)
        print(n)

sol = Solution()
sol.printNumbers(5)