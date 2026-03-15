class Solution:
    def insertionSort(self, nums):
        # cnt=0
        # while cnt<len(nums):
        #     for i in range(0,len(nums)):
        #         if nums[i]>nums[cnt]:
        #             nums[i],nums[cnt]=nums[cnt],nums[i]
        #     cnt+=1
        # return nums
        for i in range(1,len(nums)):
            key=nums[i]
            j=i-1
            while j>=0 and key<nums[j]:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums


sol=Solution()
print(sol.insertionSort([3,4,2,5,1,6]))