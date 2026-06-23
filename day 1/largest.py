number_1 =int(input("Enter Number 1:"))
number_2 =int(input("Enter Number 2:"))
number_3 =int(input("Enter Number 3:"))

if (number_1>number_2 and number_1>number_3):
    print(f"The largest number is {number_1}")
elif(number_2>number_1 and number_2> number_3):
    print(f"The largest number is {number_2}")
elif(number_1==number_2==number_3):
    print("All value are same")
elif(number_1==number_2 and number_2>number_3):
    print("number 1 and 2 same numbers")
elif(number_1==number_2 and number_2<number_3):
    print(f"The largest number is {number_3}")
elif(number_2==number_3 and number_3>number_1):
    print("number 2 and 3 same numbers")
elif(number_2==number_3 and number_3<number_1):
    print(f"The largest number is {number_1}")
elif(number_1==number_3 and number_3>number_2):
    print("number 2 and 3 same numbers")
elif(number_1==number_3 and number_3<number_2):
    print(f"The largest number is {number_2}")
else:
    print(f"The largest number is {number_3}")