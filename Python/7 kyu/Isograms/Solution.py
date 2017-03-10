def is_isogram(string):
    array = []
    string = string.upper()
    
    for string_i in range(0,(len(string))):
        #Store first character in array.
        if(string_i == 0):
            array.append(string[string_i:(string_i+1)])
        else :
            #Search array to see if character has already been seen.
            for array_i in range(0, len(array)):
                #If character is a repeat, return False.
                if(array[array_i] == string[string_i:(string_i+1)]):
                    return False
            #If character has been proven not to be a repeat, append to prior char array.
            array.append(string[string_i:(string_i+1)])
    #If no repeats were found, return True.
    return True
