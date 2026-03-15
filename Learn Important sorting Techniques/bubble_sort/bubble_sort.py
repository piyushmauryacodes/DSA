class Solution:
    def bubbleSort(self, nums):
        cnt=len(nums)-1
        while cnt>1:
            for i in range(0,cnt):
                if nums[i] > nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
            cnt-=1
        return nums



sol=Solution()
print(sol.bubbleSort([7,4,1,5,3,1]))
 