# text = input("username: ")
# number = int (text)
# print(number)

text = input("username: ")
try:
    number = int (text)
    print(number)
except:
    print("invalide udername")