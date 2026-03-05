class Solution(object):
    def isPalindrome(s):
        temp =s
        left,right=0,len(s)-1
        if left < right:
            print(temp ==s)

        print(type(right))
        print(s[0:len(s)])

Solution.isPalindrome("my Name is, piyush")