class Solution(object):
    def removeElement(self, nums, val):
        i=0
        j=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
                nums.append("_")
                i-=1
                j+=1
                continue
            i+=1
        l=len(nums)-j
        print(nums[:l])
        return l
        

sol=Solution()
n=[0,1,2,2,3,0,4,2]
v=2
print(sol.removeElement(n,v))