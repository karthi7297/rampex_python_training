name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

student = {
    "name": name,
    "age": age,
    "city": city
}
student.update({"Course": "Python"})
print(student)