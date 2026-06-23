def CountVowels(s):
    vowels = 'aeiouAEIOU'
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count
a=input("Enter a string: ")
print(CountVowels(a))