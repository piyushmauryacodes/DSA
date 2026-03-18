class Solution:
    def bubbleSort(self, nums, n=None):
        if n is None:
            n=len(nums)
        if n<=1:
            return nums
        
        for i in range(n-1):
            if (nums[i]>nums[i+1]):
                nums[i],nums[i+1]=nums[i+1],nums[i]
        
        return self.bubbleSort(nums,n-1)
        
sol=Solution()
print(sol.bubbleSort([7 ,4 ,1 ,5 ,3]))