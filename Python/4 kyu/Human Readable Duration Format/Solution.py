def format_duration(seconds):
    years = seconds // 31536000
    seconds -= years * 31536000
    days = seconds // 86400
    seconds -= days * 86400
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    print(timeString(years, days, hours, minutes, seconds))
    return timeString(years, days, hours, minutes, seconds)
    
def timeString(years, days, hours, minutes, seconds):
    time = []
    result = ""
    first = True
    
    time.append(formatVariable(years, "year"))
    time.append(formatVariable(days, "day"))
    time.append(formatVariable(hours, "hour"))
    time.append(formatVariable(minutes, "minute"))
    time.append(formatVariable(seconds, "second"))
    
    time = cleanArray(time)
            
    if len(time) == 0:
        return "now"
    elif len(time) == 1:
        return time[0]
    elif len(time) == 2:
        return time[0] + " and " + time[1]
    elif len(time) == 3:
        return time[0] + ", " + time[1] + " and " + time[2]
    else:
        for val_i in range(0, len(time)-1):
            result += time[val_i] + ", "
        return result[:-2] + " and " + time[len(time)-1]
        
def formatVariable(var, label):
    result = ""
    
    if(var > 0):
        result += str(var) + " " + label
        if(var > 1):
            result += "s"
    return result
    
def printArray(arr):
    for var in arr:
        print("|" + str(var) + "|")

def cleanArray(arr):
    for var_i in range(len(arr)*-1+1, 1):
        if arr[var_i*-1] == "":
            arr.pop(var_i*-1)
            
    return arr
