class Solution(object):
    def lengthOfLastWord(self, s):
        i=1
        splt=s.split(' ')
        print(splt)
        while i>0:
            if splt[-i]=='':
                i+=1
            else:
                return len(splt[-i])
            i+=1



sol=Solution()
print(sol.lengthOfLastWord("a "))