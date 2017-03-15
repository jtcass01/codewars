def solution(string,markers):
    pointer = 0
    result = ""

    nearestMarker = len(string)
    found = False

    for marker in markers:
        markerLoc = string.find(marker)
        if markerLoc == -1:
            None
        else:
            found = True
            if markerLoc < nearestMarker:
                nearestMarker = markerLoc
    
    if not found:
        return string.strip()
    
    while(pointer < len(string)):
        print("Pointer = " + str(pointer))
        nearestMarker = len(string)
        found = False

        #Find nearest marker.
        for marker in markers:
            markerLoc = string.find(marker, pointer)
            if markerLoc == -1:
                None
            else:
                found = True
                if markerLoc < nearestMarker:
                    nearestMarker = markerLoc

        if found:
            result += string[pointer:nearestMarker]
            if len(result) == 0:
                None
            else:
                if result[len(result)-1] == "\n":
                    None
                else:
                    result = result.rstrip()
            endMarker = string.find("\n", nearestMarker)
            if endMarker == -1:
                return result
            else:
                pointer = endMarker
        else:
            result += string[pointer:]
            result = result.rstrip()
            return result
