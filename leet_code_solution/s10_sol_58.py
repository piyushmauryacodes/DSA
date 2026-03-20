class Solution(object):
    def lengthOfLastWord(self, s):
        # i=1
        # splt=s.split(' ')
        # print(splt)
        # while i:
        #     if splt[len(splt)-1]=='':
        #         splt.pop(len(splt)-1)
        #     else:
        #         return len(splt[-1])
        #     i+=1
        word_list = s.split()
        print(word_list)
        return len(word_list[-1])


sol=Solution()
print(sol.lengthOfLastWord("hello world "))