# string = "hello world"
# print(string.count("l"))

password = input("enter passowrd\n")

if password.count("_") != 0:
    print("underscore not allowed")
else:
    print("underscore absent")