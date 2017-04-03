class character:
    def __init__(self, char):
        self.char = char
        self.count = 1
        
    def __str__(self):
        return "{char: " + str(self.char) + ", count: " + str(self.count) + "}"
        
    def equals(self, comparison):
        if(self.char.isupper()):
            if comparison.upper() == self.char:
                return True
            else:
                return False
        else:
            if comparison.lower() == self.char:
                return True
            else:
                return False
                
    def inc(self):
        self.count += 1
        
    #Getters
    def getChar(self):
        return self.char
    def getCount(self):
        return self.count
    #Setters
    def setChar(self, char):
        self.char = char
    def setCount(self, count):
        self.count = count

def first_non_repeating_letter(string):
    chars = []
    
    for char in string:
        if isNew(chars, char):
            chars.append(character(char))
        else:
            for value in chars:
                if value.equals(char):
                    value.inc()
    
    return getFirstNonRepeating(chars)

def printArray(arr):
    result = "["
    
    for val in arr:
        result += str(val) + ","
        
    print(result[:-1] + "]")
    
def getFirstNonRepeating(arr):
    for val in arr:
        if val.getCount() == 1:
            return val.getChar()
    return ""

def isNew(chars, char):
    for character in chars:
        if character.equals(char):
            return False
    return True
