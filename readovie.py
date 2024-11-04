file = open("ovie.txt", "r")
f = file.readlines()

newlist = []

for line in f:
    newlist.append(line[:-1])

print(newlist)