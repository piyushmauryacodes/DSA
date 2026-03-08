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