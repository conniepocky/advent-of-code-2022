f = open("instructions.txt", "r")

arr = f.read().split("\n")

crates = {
    1: ["V", "Q", "W", "M", "B", "N", "Z", "C"],
    2: ["B", "C", "W", "R", "Z", "H"],
    3: ["J", "R", "Q", "F"],
    4: ["T", "M", "N", "F", "H", "W", "S", "Z"],
    5: ["P", "Q", "N", "L", "W", "F", "G"],
    6: ["W", "P", "L"],
    7: ["J", "Q", "C", "G", "R", "D", "B", "V"],
    8: ["W", "B", "N", "Q", "Z"],
    9: ["J", "T", "G", "C", "F", "L", "H"]
}

# crates = {
#     1: ["N", "Z"],
#     2: ["D", "C", "M"],
#     3: ["P"]
# }


for instruction in arr:
    instruction = instruction.strip()
    instruction = instruction.split(' ')

    print(instruction)

    i = 0

    if int(instruction[1]) == 1:
        fromCrate = int(instruction[3])
        goToCrate = int(instruction[5])
        valueToAdd = crates[fromCrate][0]

        crates[goToCrate].insert(0, valueToAdd)

        crates[fromCrate].remove(valueToAdd)
    else:
        howManyTimes = int(instruction[1])
        print(howManyTimes)
        fromCrate = int(instruction[3])
        goToCrate = int(instruction[5])

        valuesToAdd = []

        newList = crates[goToCrate]

        for d in range(0, howManyTimes):
            print(crates[fromCrate][d])
            valuesToAdd.append(crates[fromCrate][d])

        for i in range (0, len(valuesToAdd)):
            crates[goToCrate].insert(i, valuesToAdd[i])

        print(crates[fromCrate])

        print(crates[goToCrate])

        for g in valuesToAdd[::-1]:
            crates[fromCrate].pop(valuesToAdd.index(g))

        print(crates)

print(crates)
