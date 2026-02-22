arr=[23,43,2,14,84,90,65]
# for i in range(0,len(arr)):
#     for j in range(0,len(arr)-1):
#         max=arr[j]
#         if(max<arr[j+1]):
#             max=arr[j+1]
# print(max)
max=arr[0] 
for n in arr:
    if(max< n):
        max=n
print(max)