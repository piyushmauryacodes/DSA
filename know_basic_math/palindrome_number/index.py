# class Solution:
#     def palindrome_check(n):
#         temp = n
#         num=0
#         while n > 0:
#             rem = n % 10
#             num= num*10+rem
#             n =n // 10
#         if num==temp :
#             print(temp," is a Palindrome Number.")
#         else:
#             print(temp," is not a Palindrome Number.")

# Solution.palindrome_check(123321)

# class solution:
#     def palindrome_check(n):
#         new_str= n[::-1]
#         if new_str==n:
#             print(n, " is a palindrome string")
#         else:
#             print(n," is not a plaindrome string")
        

# solution.palindrome_check("piyush")

class Solution(object):
    def isPalindrome(x):
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
        
print(Solution.isPalindrome(121))