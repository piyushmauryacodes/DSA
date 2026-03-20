class Solution(object):
    def removeElement(self, nums, val):
        i,j=0,0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
                nums.append(0)