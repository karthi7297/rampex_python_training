#formal way
n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


#alternative method

for i in range(1,n+1):
    print(str(i)*i)