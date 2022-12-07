f = open("input.txt", "r")

arr = list(f.read())

i = 0

notFoundMarker = True

while notFoundMarker:
    f = arr[i:(i+14)]

    if len(set(list(f))) == 14:
        print(i + 14)
        notFoundMarker = False
    
    i+=1