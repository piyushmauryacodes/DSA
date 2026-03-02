class Solution:
    def reverse_array(self,arr,n):
        if arr==[]:
            return n
        else:
            p=arr.pop()
            n.append(p)
            return self.reverse_array(arr,n)
sol= Solution()
print(sol.reverse_array([32,43,54,65,76],[]))