class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        # 2. Helper Function: Merges two separate, already-sorted arrays
        def merge_array(left, right):
            result = []
            i, j = 0, 0
            n, m = len(left), len(right)
            
            # Compare the front of both arrays and append the smaller one
            while i < n and j < m:
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            # Cleanup: Grab any leftovers from whichever array didn't finish
            # (In Python, extending a slice like this is a clean alternative to a while loop)
            result.extend(left[i:])
            result.extend(right[j:])
            
            return result

        # 3. Divide: Split the current array down the middle
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]
        
        # 4. Conquer: Recursively sort both newly created halves
        # Note: We use self.mergeSort because it's inside a class
        left_half = self.mergeSort(left_half)
        right_half = self.mergeSort(right_half)
        
        # 5. Combine: Merge the two sorted halves and return the result
        return merge_array(left_half, right_half)
    

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


