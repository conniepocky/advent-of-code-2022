f = open("input.txt", "r")

totalCalories = []

arr = f.read().split("\n")

indexOfLastStop = 0

total = 0

top3 = 0

for i in arr:

    if i == "":
        totalCalories.append(total)
        total = 0
    else:
        total += int(i)

totalCalories = sorted(totalCalories)

totalCalories.reverse()

print(totalCalories)

for i in range (0, 3):
    print(i)
    top3 += totalCalories[i]

print(top3)