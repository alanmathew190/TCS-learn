n=int(input())


# arr=list(map(int,input().split()))
    
# arr.sort()
# print(*arr)

arr=[list(map(int,input().split())) for _ in range(n)]

arr.sort(key=lambda x:(x[0],x[1]))

for i in arr:
    print(*i)

# n=int(input())
# arr=list(map(int,input().split()))[:n]
# count=0
# for i in range(len(arr)-1):
#     if arr[i]==arr[i+1]:
#         count+=1

# print(count)