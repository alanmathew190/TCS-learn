# reverse each word

# s=input()
# a=""
# arr=s.split(" ")
# for word in arr:
#     a+=word[::-1]
#     a+=" "

# print(a)


# most frequent element in array

# arr=list(map(int,input().split()))
# freq={}
# val = float("-inf")
# maxim=float("-inf")
# for num in arr:
#     freq[num]=freq.get(num,0)+1
# print(freq)
# for key,value in freq.items():
#     maxim=max(maxim,value)
#     val=freq.get(key)
# print(val)
# print(maxim)

# Remove duplicates AND maintain order

# nums=list(map(int,input().split()))
# new=[]


# for num in nums:
#     if num not in new:
#         new.append(num)
    
# print(new)


# Check if two strings are anagrams

# s1,s2=map(str,input().split())

# if len(s1)!= len(s2):
#     print("not anagram")
# else:
#     if sorted(s1)==sorted(s2):
#         print("anagram")
#     else:
#         print("not anagram")
    
# Move all negative numbers to left and positives to right

# nums=list(map(int,input().split()))
# arr=[]
# for num in nums:
#     if num<0:
#         arr.append(num)

# for num in nums:
#     if num>=0:
#         arr.append(num)
    
# print(arr)