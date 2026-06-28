n=int(input())
count=n*(n+1)//2
for i in range(n):
    for j in range(n-i):
        print(count,end="")
        count-=1
    print() 
