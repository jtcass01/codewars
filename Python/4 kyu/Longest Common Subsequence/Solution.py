import itertools

def lcs(string, subsequence):
    arr = []
    subsets = []
    result = ""
    strLocation = 0

    if len(subsequence) > 1:
        arr = list(subsequence)
    else:
        if string.find(subsequence) != -1:
            return subsequence
        else:
            return ""
  
    for L in range(0, len(arr)+1):
        for subset in itertools.combinations(arr, L):
            if(len(list(subset)) == 1):
                subsets.append("".join(list(subset)))
        
    for subset in subsets:
        if string.find(subset, strLocation) != -1 and strLocation < len(string):
            result += subset
            strLocation = string.find(subset, strLocation) + 1
            
    return result
