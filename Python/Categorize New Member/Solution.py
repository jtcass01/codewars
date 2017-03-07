def openOrSenior(data):
    resultantList = []

    #Loop through data
    for data_i in range(0, len(data)):
        #If both requirements are met, label location Senior
        if(data[data_i][0] >= 55 and data[data_i][1] > 7):
            resultantList.append('Senior')
        #If not, label location Open
        else:
            resultantList.append('Open')
    
    return resultantList
