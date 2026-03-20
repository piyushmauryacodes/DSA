# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        res=[]
        i,j=0,0
        n=len(list1)
        m=len(list2)
        while i<n and j<m:
            if list1[i]<=list2[j]:
                res.append(list1[i])
                i+=1
            else:
                res.append(list2[j])
                j+=1
        res.extend(list1[i:])
        res.extend(list2[j:])
        return res
        
sol=Solution()
l1=[]
l2=[]
print(sol.mergeTwoLists(l1,l2))