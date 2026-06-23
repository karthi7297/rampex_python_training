a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
sum=0
for i in range(a,b+1):
    sum+=i
avg=sum/(b-a+1)
print(avg)