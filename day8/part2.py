f = open("input.txt", "r")
 
arr = f.read().splitlines()
 
rows = []
columns = []
 
index = 0
 
rows = arr

scenicScores = []

for i in range(0, len(rows)):
    column = [item[i] for item in rows]
 
    columns.append(column)
 
 
def isVisibleDown(i, col):
    col = [x for x in col if x != '']
    col = [int(x) for x in col]

    count = 0
 
    for f in reversed(range(0, len(col))):
        if f == i:
            break
        if col[f] >= col[i]:
            count += 1
            return count
        count += 1
 
    return count
 
 
def isVisibleUp(i, col):
    col = [x for x in col if x != '']
    col = [int(x) for x in col]

    count = 0

    for f in range(0, i):
        if col[f] >= col[f + 1] and col[f] >= col[i]:
            return f+1
        count += 1
 
    return count
 
 
def isVisibleLeft(i, row):
    row = list(row)
    row = [int(x) for x in row]

    count = 0
 
    for f in range(0, i):
        if row[f] >= row[f + 1] and row[f] >= row[i]:
            return f+1
        count += 1
 
    return count
 
 
def isVisibleRight(i, row):
    row = list(row)
    row = [int(x) for x in row]

    count = 0

    for f in reversed(range(0, len(row))):
        if f == i:
            break
        if row[f] >= row[i]:
            count += 1
            return count
        count += 1
 
    return count
 
 
for iRow, row in enumerate(rows):
    if iRow == 0 or iRow == len(rows) - 1:
        scenicScores.append(0)
    else:
        for i, value in enumerate(row):
            print("value", value)
            print("row", list(row))
            print("column", columns[i])
            print("left", isVisibleLeft(i, row))
            print("right", isVisibleRight(i, row))
            print("down", isVisibleDown(iRow, columns[i]))
            print("up", isVisibleUp(iRow, columns[i]))
            scenicScores.append(isVisibleLeft(i, row) * isVisibleRight(i, row) * isVisibleUp(
                    iRow, columns[i]) * isVisibleDown(iRow, columns[i]))
            print("\n")

print(scenicScores)
print(max(scenicScores))