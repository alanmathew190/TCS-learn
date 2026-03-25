n=int(input())
marks=list(map(str,input().split(',')))
markmap={}
m=[]
for mark in marks:
    m.append(mark.split(":"))
    
for det in m:
    markmap[det[0]]=int(det[1])

for key, value in markmap.items():
    print(key,value)