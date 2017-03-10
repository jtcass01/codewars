def likes(names):
    names_length = len(names)
    result = ''
    
    if(names_length == 0):
        result = "no one "
    elif(names_length == 1):
        result = names[0] + " "
    elif(names_length == 2):
        result = names[0] + " and " + names[1] + " "
    elif(names_length == 3):
        result = names[0] + ", " + names[1] + " and " + names[2] + " "
    elif(names_length > 3):
        result = names[0] + ", " + names[1] + " and " + str(names_length-2) + " others "
    if(names_length > 1):
        return result + "like this"
    else:
        return result + "likes this"    
