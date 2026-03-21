#subarrays with given sum from array

arr=list(map(int,input().split())) #if input is array use this line
t= int(input())# if input is single digit use this line

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if sum(arr[i:j])==t:
            print(arr[i:j])
        