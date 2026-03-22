arr=list(map(int,input().split()))
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
for key in freq:
    if freq[key]==1:
        print(key)
print(freq)


mx=float("-inf")
for key,value in freq.items():
    mx=max(mx,freq[key])

for key in freq:
    if mx==freq[key]:
        ans=key
print(ans)