n=list(map(int,input().split()))
EvenCount=0
OddCount=0
for i in n:
    if i%2==0:
        EvenCount+=1
    else:
        OddCount+=1
print("EvenCount:",EvenCount)
print("OddCount:",OddCount)