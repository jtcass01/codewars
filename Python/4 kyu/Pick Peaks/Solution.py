def pick_peaks(arr):
    print(arr)
    pos = []
    peaks = []
    for arr_i in range(0, len(arr)):
        if(arr_i == 0):
            None
        elif(arr_i == len(arr)-1):
            None
        else:
            if(arr[arr_i] > arr[arr_i+1] and arr[arr_i] > arr[arr_i-1]):
                pos.append(arr_i)
                peaks.append(arr[arr_i])
            elif(arr[arr_i] == arr[arr_i+1] and arr[arr_i] > arr[arr_i-1]):
                for arr_j in range(arr_i, len(arr)):
                    if arr[arr_j] < arr[arr_i]:
                        pos.append(arr_i)
                        peaks.append(arr[arr_i])
                        break
                    elif arr[arr_j] > arr[arr_i]:
                        break
                
    result = {'pos': pos, 'peaks': peaks}
    
    return result
