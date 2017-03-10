def add_binary(a,b):
    binaryString = ""
    #Add two integers
    a += b
    
    #If the sum of the two integers is 0, return 0
    if (a == 0):
        return "0"
    #If the sum is greater than 0, run algorithm
    else:
        #While a is greater than or equal to 1, find remainder of sum divded by 2
        while(a >= 1):
            #If remainder is 0, add 0 to the left most location of string
            if(a%2 == 0):
                binaryString = "0" + binaryString
            #If remainder is 1, add 1 to the left most location of string
            else:
                binaryString = "1" + binaryString
            #Divide a by 2 and then repeat above steps.
            a /= 2
    return binaryString
