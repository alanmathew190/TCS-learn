words=list(map(str,input().split()))
countmap={}
count=float("-inf")
for word in words:
    countmap[word]=countmap.get(word,0)+1
    
for key,value in countmap.items():
    if value>count:
        count=value
        w=key
    else:
        if value==count:
            if w>key:
                w=key
print(w)