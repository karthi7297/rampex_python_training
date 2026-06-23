n = list(map(int, input("Enter numbers: ").split()))

count_dic = {}

for i in n:
    if i in count_dic:
        count_dic[i] += 1
    else:
        count_dic[i] = 1

print(count_dic)