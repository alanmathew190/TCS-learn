n=int(input())
mp={}
ans=[]
for i in range(n):
    a,b,c,d=map(str,input().split())
    c=int(c)
    d=int(d)
    key=(a,b)
    
    if key in mp:
        if abs(d-mp[key])<=60:
            ans.append([a,b,c,d])
    mp[key]=d

for i in ans:
    print(*i)