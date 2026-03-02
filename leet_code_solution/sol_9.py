class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        if s[0]=="-":
            rev=s[:0:-1]+"-"
        else:
            rev=s[::-1]
        if -2**31<=x<=2**31:
            if rev==s:
                return rev==s
            else:
                return rev==s
        else:
            return 0