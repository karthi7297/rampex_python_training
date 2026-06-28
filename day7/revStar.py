n=int(input())
top=(n//2)
bottem=n-top
for i in range(1,n+1):
    if (i<=top):
        print(i*"*")
    else:
        print("*"*bottem)
        bottem-=1


    