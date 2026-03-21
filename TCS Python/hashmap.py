# arr=list(map(int,input().split()))
# s=input()
# freq={}

# for i in s:
#     freq[i]=freq.get(i,0)+1
# for key, value in freq.items():
#     print(key, value)
    
# print(freq)


#First Non-Repeating Character
# s=input()

# freq={}

# for ch in s:
#     freq[ch]=freq.get(ch,0)+1
    
# for ch in s:
#     if freq[ch]==1:
#         print(ch)
#         break

#index of First Non-Repeating Character
s=input()

freq={}

for ch in s:
    freq[ch]=freq.get(ch,0)+1
    
for i  in range(len(s)):
    if freq[s[i]]==1:
        print(i)
        break
