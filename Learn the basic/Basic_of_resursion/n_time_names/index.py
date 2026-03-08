class Solution():
    def repeat_name(self,n):
        if n==0:
            return ""
        else:
            return "Piyush " + self.repeat_name(n-1)
sol = Solution()

print(sol.repeat_name(4))