def is_valid_coordinates(coordinates):
    coordinates = coordinates.split(",")
    if(len(coordinates) != 2):
        return False    
    
    latitude = coordinates[0]
    longitude = coordinates[1]
    
    if(testLongitude(longitude) and testLatitude(latitude)):
        return True
    else:
        return False

def testLatitude(lat):
    if(is_numeric(lat)):
        lat = float(lat)
        
        if abs(lat) < 0 or abs(lat) > 90:
            return False
        else:
            return True
    else:
        return False

def testLongitude(long):
    if(is_numeric(long)):
        long = float(long)
        
        if abs(long) < 0 or abs(long) > 180:
            return False
        else:
            return True
    else:
        return False

def is_numeric(s):
    print(s)
    if(s.count(".") > 1 or s.count(" ") > 1 or s.count(",") > 0 or s.count("e") > 0):
        return False
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError, ValueError):
        pass
    return False
