class Solution:
    def print_numbers(self,n):
        if n ==0:
            return
        else:
            print(n)
            self.print_numbers(n-1)

sol=Solution()
print(sol.print_numbers(8))