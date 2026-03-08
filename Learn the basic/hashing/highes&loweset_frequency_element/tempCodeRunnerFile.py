class Solution:
    def mostFrequentElement(self, nums):
        hash_list=[0]*len(nums)
        for num in nums:
            hash_list[num]+=1
        for cnt, frequency in enumerate(hash_list):
            if frequency>0:
                
                return hash_list
    
        

sol=Solution()