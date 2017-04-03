import itertools

def next_bigger(n):
    nums = []
    possibilities = []
    possibility = ""
    
    nums = list(str(n))
    
    for subset in itertools.permutations(nums, len(str(n))):
        possibility = int("".join(list(subset)))
        if possibilities.count(possibility) == 0:
            possibilities.insert(0, possibility)

    possibilities.sort()

    current = possibilities.index(n)
    
    if(current != len(possibilities)-1):
        return possibilities[current+1]
    else:
        return -1
