def solution(digits):
    max = digits[0:5]
    for digits_i in range(0, len(number)-5):
        testNum = digits[digits_i:digits_i+5]
        if(testNum > max):
            max = testNum
    return int(max)
