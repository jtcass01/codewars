import itertools

def get_pins(observed):
    result = []
    possibilityMatrix = []

    result.append(observed)

    for num in observed:
        possibilityArray = []
        positionArray = []
        #Find positionArray
        for array_i in range(0, len(numMatrix)):
            for num_i in range(0, len(numMatrix[array_i])):
                if(numMatrix[array_i][num_i] == num):
                    positionArray.append(array_i)
                    positionArray.append(num_i)
                    print(positionArray)
        possibilityArray.append(num)
        #check left
        if (positionArray[1] < 3) and (int(positionArray[0]) - 1 >= 0):
            possibilityArray.append(numMatrix[positionArray[0]-1][positionArray[1]])
        #check right
        if (positionArray[1] < 3) and (int(positionArray[0]) + 1 <= 2):
            possibilityArray.append(numMatrix[positionArray[0]+1][positionArray[1]])
        #check top
        if (positionArray[1] > 0):
            possibilityArray.append(numMatrix[positionArray[0]][positionArray[1]-1])
        #check bottom
        if (positionArray[0] == 1):
            if (positionArray[1] < 3):
                possibilityArray.append(numMatrix[positionArray[0]][positionArray[1]+1])
        else:
            if (positionArray[1] < 2):
                possibilityArray.append(numMatrix[positionArray[0]][positionArray[1]+1])

        possibilityMatrix.append(possibilityArray)

    if(len(possibilityMatrix) < 2):
        return possibilityMatrix[0]
    else:
        return combineMatrix(possibilityMatrix)
        
def combineMatrix(matrix):
    result = []

    for arr in list(itertools.product(*matrix)):
        result.append("".join(arr))

    return result
