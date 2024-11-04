file = open("file.txt", "r")
f = file.readlines()

Newlist = []

for line in f:
    Newlist.append(line[:-1])

print(Newlist)
