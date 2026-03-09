class Solution:
    def countFrequencies(self,nums):
        hash_list=[0]*(max(nums)+1)
        arr=[]
        for num in nums:
            hash_list[num]+=1
        
        for cnt, frequency in enumerate(hash_list):
            if frequency > 0:
                arr.append([cnt, frequency])
        return arr


sol=Solution()
# n=int(input("Enter the size of array: "))
# arr=[]
# while n>=1:
#     num=int(input("Enter your element no. "))
#     arr.append(num)
#     n-=1


print(sol.countFrequencies([1,2,2,1,3,5]))




# class Solution(object):
#     def maxFrequency(self, nums, k):
#         nums.sort()
#         l,r=0,0
#         total,res=0,0
#         while r < len(nums):
#             total+=nums[r]
#             while nums[r]*(r-l+1)>total +k:
#                 total-=nums[l]
#                 l+=1
#             res = max(res,r-l+1)
#             r+=1
#         return res