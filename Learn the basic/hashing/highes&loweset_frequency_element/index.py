class Solution:
    def mostFrequentElement(self, nums):
        arr=[]
        hash_list=[0]*(max(nums)+1)
        for num in nums:
            hash_list[num]+=1
        for cnt, frequency in enumerate(hash_list):
            if frequency>0:
                arr.append([cnt,frequency])
                most_frequent_num=max(arr,key=lambda x:x[1])
        return most_frequent_num[0]
        

sol=Solution()
nums=[4,4,5,5,6]
print(sol.mostFrequentElement(nums))