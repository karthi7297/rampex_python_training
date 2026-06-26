class InvalidMarkError(Exception):
    pass
try:
    mark=int(input("Enter your mark:"))
    if mark < 0 or mark > 100:
        raise InvalidMarkError("Invalid mark. Please enter a mark between 0 and 100.")
    else:
        print("Your mark is:", mark)
except InvalidMarkError as e:
    print(e)