class Solution:
    def mergeSort(self, nums):
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left_half=nums[:mid]
        right_half=nums[mid:]
        left_half=mergeSort(left_half)
        right_half=mergeSort(right_half)
        return merge_array(left_half,right_half )
        # st=0
        # end=len(nums)-1
        # def merge(nums,st,mid,end):
        #     temp=[]
        #     i,j=st,mid+1
        #     while(i<=mid and j<=end):
        #         if(nums[i]<nums[j]):
        #             temp.append(nums[i])
        #             i+=1
        #         else:
        #             temp.append(nums[j])
        #             j+=1
        #     while i<=mid:
        #         temp.append(nums[i])
        #         i+=1
        #     while j<=end:
        #         temp.append(nums[j])
        #         j+=1
        #     for k in range(len(temp)):
        #         nums[st+k]=temp[k]


        # def ms(nums,st,end):
        #     if st>=end:
        #         return
        #     mid=(st+end)//2
        #     ms(nums,st,mid)       #left half
        #     ms(nums,mid+1,end)    #right half
        #     merge(nums,st,mid,end)

        # ms(nums,st,end)
        # return nums
        
        




sol=Solution()
print(sol.mergeSort([3,4,2,6,1,3,6]))


