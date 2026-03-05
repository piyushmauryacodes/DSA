class Solution(object):
    def fib(self, n):
        if n<=0 or n>30:
            return 0
        num=n
        arr=[0,1]
        a=0
        b=1
        for i in range(num):
            temp=a+b
            arr.append(temp)
            a=b
            b=temp
        sum_fab=arr[n-1]+arr[n-2]
        return sum_fab

