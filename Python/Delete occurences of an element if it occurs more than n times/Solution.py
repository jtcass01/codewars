def delete_nth(order,max_e):
    numList = []
    numList.append([order[0], 1])
    resultantList = []
    resultantList.append(order[0])

    for order_i in range(1,len(order)):
        numFound = False
        for numList_i in range(0, len(numList)):
            if(numList[numList_i][0] == order[order_i]):
                numList[numList_i][1] += 1
                numFound= True
                if(numList[numList_i][1] <= max_e):
                    resultantList.append(order[order_i])
        if(numFound == False):
            numList.append([order[order_i], 1])
            resultantList.append(order[order_i])
    return resultantList
