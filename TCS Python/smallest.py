arr=list(map(int,input().split()))
minel=float('inf')
secminel=float('inf')
maxel=float('-inf')

for i in range(len(arr)):
    if arr[i]<minel:
        secminel=minel
        minel=arr[i]
    # minel=min(minel,arr[i])
    # maxel=max(maxel,arr[i])
print(secminel)
print(minel)
# print(maxel)
arr.sort()
print(arr)
print(arr[0]) #smallest
print(arr[len(arr)-1]) #largest
print(arr[1]) #second smallest
print(arr[len(arr)-2]) # second largest

