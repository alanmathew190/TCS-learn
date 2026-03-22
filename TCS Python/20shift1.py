# num=int(input())

# if num<=0:
#     print("Invalid input")
# elif num==1:
#     print("Cost: 2000")
# elif num>=2 and num<=3:
#     print("Cost: 5000")
# elif num>=4 and num<=5:
#     print("Cost: 9000")
# elif num>6:
#     print("Cost: 15000")
    
#fraudtransactions

# t=int(input())
# mp={}

# fraud = []

# for i in range(t):
#     s,r,amt,time=input().split()
#     amt=int(amt)
#     time=int(time)
    
#     key=(s,r,amt)
    
#     if key in mp:
#         if time - mp[key] <= 60:
#             print(s, r, amt, time)

#     mp[key] = time


# amount=float(input())

# if amount<1000:
#     print(amount-(amount*5//100))
# elif amount>=1000 and amount<5000:
#     print(f"{amount-(amount*10//100):.2f}")
# elif amount>=5000:
#     print(amount-(amount*15//100))


# n = int(input())
# arr = []

# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# # sort by first element, then second
# arr.sort(key=lambda x: (x[0], x[1]))

# for i in arr:
#     print(i[0], i[1])


