n=int(input("Enter the number of elements in the list: "))
l1=[]
l2=[]
for i in range(n):
    
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
print("Even numbers are: ",l1)
print("Odd numbers are: ",l2)