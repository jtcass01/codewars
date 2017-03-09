def in_array(array1, array2):
    result = []
    
    for array1_i in array1:
        for array2_i in array2:
            if array1_i in array2_i:
                if array1_i in result:
                    None
                else:
                    result.append(array1_i)
                    break
    result.sort()
    return result
