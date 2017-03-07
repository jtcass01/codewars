def get_sum(a,b):
    total = 0;

    if(a==b):
        return a
    elif(a>b):
        for num in range(a,(b+1)):
            total += num
    else:
        for num in range(b,(a+1)):
            total += num

    return total
