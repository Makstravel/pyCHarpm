class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


s = input().split()
for i in s:
    if hasattr(Person, i.lower()):
        print(f' {i}-YES')
    else:
        print(f' {i}-NO')
