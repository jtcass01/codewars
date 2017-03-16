def spiralize(size):
    assert(size >=0)

    if size == 1:
        return [[1]]
    elif size == 2:
        return [[1,1],[0,1]]
    elif size == 3:
        return [[1,1,1],[0,0,1],[1,1,1]]
    elif size == 0:
        return []
    
    arr = []
    placeHolderX = 0
    placeHolderY = 1
    h = True
    right = True
    down = True
    lineSize = size - 1

    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(1)
        arr.append(row)

    while(1):
        if h:
            if right:
                stop = findPath(arr, placeHolderY, placeHolderX, "h")
                right = False
            else:
                stop = findPath(arr, placeHolderY, placeHolderX, "-h")
                right = True
            if stop == -1:
                break
            else:
                walkPath(arr, placeHolderY, placeHolderX, stop, "h")
                placeHolderX = stop
                h = False
        else:
            if down:
                stop = findPath(arr, placeHolderX, placeHolderY, "v")
                down = False
            else:
                stop = findPath(arr, placeHolderX, placeHolderY, "-v")
                down = True
            if stop == -1:
                break
            else:
                walkPath(arr, placeHolderX, placeHolderY, stop, "v")
                placeHolderY = stop
                h = True
#        printArray(arr)
#        print("")
    printArray(arr)
    return arr
    

def walkPath(array, line, start, stop, mode):
    temp = 0
    if stop < start:
        temp = stop
        stop = start
        start = temp
        stop += 1
    else:
        stop += 1
    
    if mode == "v":
        for i in range(start, stop):
            array[i][line] = 0
    elif mode == "h":
        for i in range(start, stop):
            array[line][i] = 0

def findPath(array, line, start, direction):
    if direction == "h":
        if array[line][start+2] == 0 or array[line][start+1] == 0:
            return -1
        else:
            for i in range(start+1, len(array)):
                if array[line][i] == 0:
                    return i-2
            return len(array) - 2
    elif direction == "v":
        if array[start+2][line] == 0 or array[start+1][line] == 0:
            return -1
        else:
            for i in range(start+1, len(array)):
                if array[i][line] == 0:
                    return i-2
            return len(array) - 2
    elif direction == "-h":
        if array[line][start-2] == 0 or array[line][start-1] == 0:
            return -1
        else:
            for i in range((start*-1)+1, 0):
                if array[line][i*-1] == 0:
                    print((i*-1)+1)
                    return (i*-1)+2
            return 1
    else:
        if array[start-2][line] == 0 or array[start-1][line] == 0:
            return -1
        else:
            for i in range((start*-1)+1,0):
                if array[i*-1][line] == 0:
                    return (i*-1) + 2                
            return 1
        

def printArray(arr):
    for row in arr:
        print(row)
