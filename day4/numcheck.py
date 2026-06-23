n=list(map(int,input().split()))
a = int(input("Enter the number to check: "))
if a in n:
    print("Number is present in the list")
else:
    print("Number is not present in the list")