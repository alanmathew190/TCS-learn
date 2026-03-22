# n = int(input())
# arr=[0]*n
# print(arr)


arr=list(map(int,input().split()))
# arr.sort(reverse=True)
# print(arr)


# arr=[list(map(int,input().split())) for _ in range(n)]

# arr.sort(key=lambda x:x[1])

# arr.sort(key=lambda x:(x[0],x[1]))
arr.sort(key=lambda x:x%100)

print(arr)