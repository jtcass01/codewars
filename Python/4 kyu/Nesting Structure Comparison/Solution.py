def same_structure_as(original,other):
    print("original", original)
    print("other", other)
    return compare(original, other)

def compare(v1, v2):
    print("v1",v1)
    print("v2",v2)
    
    if(isinstance(v1, list) and isinstance(v2,list)):
        if len(v1) == len(v2):
            for value_i in range(0, len(v1)):
                if compare(v1[value_i], v2[value_i]) == False:
                    return False
        else:
            return False
    elif(isinstance(v1, list) or isinstance(v2,list)):
        return False
    else:
        return True
    return True
