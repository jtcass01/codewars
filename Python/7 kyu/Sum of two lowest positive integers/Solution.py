def sum_two_smallest_numbers(numbers):
    lowNum1 = numbers[0]
    lowNum2 = numbers[1]
    
    #Find lowest number, set equal to lowNum1
    for numbers_i in range(0,len(numbers)):
        if(lowNum1 > numbers[numbers_i]):
            lowNum1 = numbers[numbers_i]
    #Find second lowest number, set equal to lowNum2
    for numbers_i in range(0, len(numbers)):
        if(lowNum2 > numbers[numbers_i] and numbers[numbers_i] != lowNum1):
            lowNum2 = numbers[numbers_i]
    #Add two numbers and return.
    return lowNum1 + lowNum2
