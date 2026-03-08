# class Solution:
#     def reverse_array(self,arr,n):
#         if arr==[]:
#             return n
#         else:
#             p=arr.pop()
#             n.append(p)
#             return self.reverse_array(arr,n)
# sol= Solution()
# print(sol.reverse_array([32,43,54,65,76],[]))

class Solution:
    def reverse_arr(self,arr:list, n:int):
        i=len(arr)-n
        if(i>=(n-1)):
            return arr
        arr[i],arr[n-1]=arr[n-1],arr[i]
        return self.reverse_arr(arr,n-1)


arr=[23,43,25,35,78,30]
n = len(arr)
sol= Solution()
print(sol.reverse_arr(arr,n))