def solution(args):
    recent = []
    ranges = []
    result = ""
    last = args[0]

    for argument in args:
        if argument == last+1 or argument == last-1:
            recent.insert(0,argument)
        else:
            if(len(recent) > 0):
                ranges.append(appendRange(recent))
                recent = clear(recent)
            recent.insert(0,argument)
        last = argument


    if(len(recent) > 0):
        ranges.append(appendRange(recent))

    return ",".join(ranges)

def appendRange(nums):
    if(len(nums) == 1):
        return str(nums[0])
    elif(len(nums) == 2):
        return str(nums[1]) + "," + str(nums[0])
    else:
        return str(nums[len(nums)-1]) + "-" + str(nums[0])

def clear(arr):
    for value_i in range(0,len(arr)):
        arr.pop(0)

    return arr

def printArray(arr):
    string = "["

    for value in arr:
        string += str(value) + ","

    print(string[:-1] + "]")
