class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        
        # 'j' scans the rest of the array starting from the second element
        for j in range(1, len(nums)):
            # If the Scout finds a value different from our current Collector's value
            if nums[j] != nums[i]:
                # Move the Collector forward
                i += 1
                # Copy the Scout's value to the Collector's new position
                nums[i] = nums[j]
        
        # Return the count of unique elements (index + 1)
        return nums[:i+1]
        

sol=Solution()
print(sol.removeDuplicates([1,1,2,3,4,5,7,7,7,7,7,7]))

