class Solution:
    def selectionSort(self, nums):
        l=0
        length=len(nums)
        while l<length:
            min_value=min(nums[l:])
            min_idx=nums.index(min_value,l)
            nums[l],nums[nums.index(min_value,l)]=nums[min_idx],nums[l]
            l+=1
        return nums
        
sol=Solution()
print(sol.selectionSort([2,1,3,5,6]))   