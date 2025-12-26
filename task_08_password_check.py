password = 12345
user = int(input("Enter password: "))

while user != password:
    print("Wrong password")
    user = int(input("Enter password again: "))

print("Access Granted!")
