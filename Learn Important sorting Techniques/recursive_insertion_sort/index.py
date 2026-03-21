class Solution:
    def insertionSort(self, nums,n=None):
        if n==None:
            n=1
        if n==len(nums):
            return nums
        key=nums[n]
        j=n-1
        while j>=0 and key<nums[j]:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
        return self.insertionSort(nums,n+1)



sol=Solution()
print(sol.insertionSort([1,2,3,1,4,6,5]))