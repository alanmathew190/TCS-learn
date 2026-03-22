
hrs=int(input())
if hrs<=0:
    print("Invalid Hours")

elif hrs>0 and hrs<=2:
    print(hrs*100)
elif hrs>2 and hrs<=5:
    print((2*100)+(hrs-2)*50)
elif hrs>5:
    print(200+150+(hrs-5)*20)