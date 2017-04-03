def countBits(n):
    bitStr = "{0:b}".format(n)
    count = 0
    
    for str_i in range(0, len(bitStr)):
        if bitStr[str_i] == "1":
            count += 1
    
    return count
