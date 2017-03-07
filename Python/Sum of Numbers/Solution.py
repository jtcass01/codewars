def get_sum(a,b):
    total = 0;
    
    #If a and b are equal, return a.
    if(a==b):
        return a
    #If a is greater than b, count from b to a and add each integer.  Return total.
    elif(a>b):
        for num in range(b,(a+1)):
            total += num
        return total
    #If b is greater than a, count from a to b and add each integer.  Return total.
    else:
        for num in range(a,(b+1)):
            total += num
        return total
