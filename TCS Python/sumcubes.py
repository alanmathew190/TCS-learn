n=int(input())
m=int(input())
 #if the input is in one line use n,m=map(int,input().split())

s=0

for i in range(n,m+1):
    s+=i*i*i
    
print(s)