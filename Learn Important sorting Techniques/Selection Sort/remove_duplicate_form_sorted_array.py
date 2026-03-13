class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        # 'i' is the slow pointer that tracks the position of the last unique element.
        i = 0
        
        # 'j' is the fast pointer that iterates through the rest of the array.
        for j in range(1, len(nums)):
            # When we find a new unique element...
            if nums[j] != nums[i]:
                # Move the slow pointer forward...
                i += 1
                # And update the array at that new position.
                nums[i] = nums[j]
                
        # The number of unique elements is the index 'i' plus 1.
        return i + 1