class Solution(object):
    def addBinary(self, a, b):
        res = ""
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            total_sum = carry
            if i >= 0:
                total_sum += int(a[i])
                i -= 1
            if j >= 0:
                total_sum += int(b[j])
                j -= 1
            res = str(total_sum % 2) + res
            carry = total_sum // 2
        return res

sol=Solution()
print(sol.addBinary("1010","1011"))