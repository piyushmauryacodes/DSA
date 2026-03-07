class Solution:
    def countFrequencies(self,nums):
        hash_list=[0]*len(nums)
        arr=[]
        cnt=0
        for num in nums:
            hash_list[num]+=1
        
        for num in hash_list:
            ar=[]
            ar.append([cnt,num])
            cnt+=1
            arr+=ar
        return arr


sol=Solution()
n=int(input("Enter the size of array: "))
arr=[]
while n>=1:
    num=int(input("Enter your element no. "))
    arr.append(num)
    n-=1


print(sol.countFrequencies(arr))