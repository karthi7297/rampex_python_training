n=(1,3,5,7,9,7,13,1,5,19)
element=int(input("Enter the element to count: "))
count=0
for i in n:
    if i==element:
        count+=1
print(count)