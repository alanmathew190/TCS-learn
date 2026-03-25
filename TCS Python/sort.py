# arr=list(map(int,input().split()))
# arr.sort() #sorted inplace
# # newarr=sorted(arr)stored in  new array 
# print(arr)

n=int(input())
line=input()

parts=line.split(",")
arr=[]
for part in parts:
    a,b=map(int,part.split()) 
    arr.append([a,b])

for i in arr:
    print(*i,end=", ")

