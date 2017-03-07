def persistence(n):
    multiCount = 0

    #If n is less than 10, return 0
    if(n<10):
        return 0
    else:
        #While n is greater than 9, multiply each digit in the number from left to right,
        #Then repeat on the result until it is less than 10, then return cycle count.  
        while(n>9):
            strN = str(n)
            nums = []
            multi = 1
            for strN_i in range(0, len(strN)):
                nums.append(strN[strN_i:(strN_i+1)])
            for num in range(0, len(nums)):
                multi *= int(nums[num])
            n = multi
            multiCount += 1
        return multiCount
