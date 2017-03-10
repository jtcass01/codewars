def sum_dig_pow(a, b):
    result = []
    
    for i in range(a,b+1):
        total = 0
        addCount = 0

        for num in str(i):
            total += int(num)**(addCount+1)
            addCount += 1
            if(total > i):
                break
        if(total == i):
            result.append(i)

    return result
