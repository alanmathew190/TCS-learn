n=int(input())

mp={}
val=[]
fraud=False
for i in range(n):
    a,b,c,d=map(int,input().split())
    
    key=(a,b,c)
    val.append(d)

    mp[key]=mp.get(key,0)+1
print(val)
if mp[key]!=n:    
    print("Its different users")
  
for i in range(len(val)-1):
    if abs(val[i]-val[i+1])<=50:
        fraud=True
    
if fraud==True:
    print("fraud")
else:
    print("Good")
    