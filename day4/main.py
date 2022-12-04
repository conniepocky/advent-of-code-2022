f = open("input.txt", "r")

arr = f.read().split("\n")

total = 0

for i in arr:
    line = i.split(",")

    firstRangeList = line[0].split("-")

    firstRange = []

    secondRangeList = line[1].split("-")

    secondRange = []

    for f in range(int(firstRangeList[0]), int(firstRangeList[1])+1):
        firstRange.append(f)

    for f in range(int(secondRangeList[0]), int(secondRangeList[1])+1):
        secondRange.append(f)

    contains =  any(item in firstRange for item in secondRange) or any(item in secondRange for item in firstRange)
    
    if contains == True:
        total += 1

print(total)

