from termcolor import colored
 
f = open("input.txt", "r")
 
arr = f.read().splitlines()
 
rows = []
columns = []
 
visible = 0
 
index = 0
 
rows = arr

for i in range(0, len(rows)):
    column = [item[i] for item in rows]
 
    columns.append(column)
 
 
def isVisibleUp(i, col):
    col = [x for x in col if x != '']
    col = [int(x) for x in col]
 
    for f in reversed(range(0, len(col))):
        if f == i:
            break
        if col[f] >= col[i]:
            return False
 
    return True
 
 
def isVisibleDown(i, col):
    col = [x for x in col if x != '']
    col = [int(x) for x in col]

    for f in range(0, i):
        if col[f] >= col[f + 1] and col[f] >= col[i]:
            return False
 
    return True
 
 
def isVisibleLeft(i, row):
    row = list(row)
 
    row = [int(x) for x in row]
 
    for f in range(0, i):
        if row[f] >= row[f + 1] and row[f] >= row[i]:
            return False
 
    return True
 
 
def isVisibleRight(i, row):
    row = list(row)
    row = [int(x) for x in row]
    for f in reversed(range(0, len(row))):
        if f == i:
            break
        if row[f] >= row[i]:
            return False
 
    return True
 
 
for iRow, row in enumerate(rows):
    if iRow == 0 or iRow == len(rows) - 1:
        for i, value in enumerate(row):
            print(colored(str(int(value)), "grey", "on_green"), end="")
        visible += len(row)
    else:
        for i, value in enumerate(row):
            if isVisibleLeft(i, row) or isVisibleRight(i, row) or isVisibleUp(
                    iRow, columns[i]) or isVisibleDown(iRow, columns[i]):
                print(colored(str(int(value)), "grey", "on_green"), end="")
                visible += 1
            else:
                print(int(value), end="")
    print("")

print(visible)