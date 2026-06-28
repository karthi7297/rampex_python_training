n=int(input())
b={i:"even" if i%2==0 else "Odd" for i in range(1,n+1)}
print(b,end='\n')