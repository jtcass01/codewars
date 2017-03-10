def make_readable(seconds):
    timeArray = []
    result = ""
    
    hours = seconds / 3600
    seconds -= hours * 3600
    
    timeArray.append(hours)

    minutes = seconds / 60
    seconds -= minutes * 60

    timeArray.append(minutes)
    timeArray.append(seconds)

    for timeArray_i in range(0,3):
        if(timeArray[timeArray_i] < 10):
            result+= "0" + str(timeArray[timeArray_i])
            if(timeArray_i < 2):
                result += ":"
        else:
            result+= str(timeArray[timeArray_i])
            if(timeArray_i < 2):
                result += ":"

    return result
