import numpy as np

f = open("input.txt", "r")

e = f.read()
arr =  map(str.split, e.splitlines())

directories = {}

currentDir = []

finalTotal = 0

print(arr)

for command in arr:
    total = 0
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                currentDir.pop()
            else:
                currentDir.append(command[2])
    elif command[0] != "dir":
        for i in range(0, len(currentDir)):
            if tuple(currentDir[: i + 1]) not in directories:
                directories[tuple(currentDir[: i + 1])] = 0
            # print([str(currentDir[i])])
            # print(command[0])
            print(tuple(currentDir[: i+ 1]))
            directories[tuple(currentDir[: i + 1])] += int(command[0])

def findClosest(list, num):
    finalList = []
    for s in list:
        if s >= num:
            finalList.append(s)

    return min(finalList)

unused = 70000000 - directories[('/'),]

values = directories.values()

required = 30000000 - (unused)

print("required ", required)

print("to delete", findClosest(values,required))

for i in values:
    if i < 100000:
        finalTotal += i

print(finalTotal)