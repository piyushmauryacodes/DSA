class Solution(object):
    def removeDuplicates(self, nums):
        print(len(nums))
        print(nums)
        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]             
        return len(nums)
    

sol=Solution()
print(sol.removeDuplicates([1,1,2,3,4,5,7,7,7,8,8,9]))

