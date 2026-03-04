class Solution(object):
    def isPalindrome(s):
        st=s.replace(" ","")
        left,right=0,len(st)-1
        print(type(right))
        print(st[0:len(st)])

Solution.isPalindrome("piyush is a good boy")