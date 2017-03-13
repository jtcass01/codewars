class Vector:
    def __init__(self, arr=[]):
        self.arr = arr

    def __str__(self):
        string = "("
        
        for i in range(0, self.length()):
            if (i < self.length()-1):
                string += str(self.get(i)) + ","
            else:
                string += str(self.get(i)) + ")"
        return (string)
        
    def length(self):
        return len(self.arr)

    def get(self, index):
        return self.arr[index]

    def push(self, val):
        self.arr.append(val)
        
    def equals(self, other):
        if(self.length() != other.length()):
            return False
        for i in range(0, self.length()):
            if(self.get(i) != other.get(i)):
                return False
        return True

    def add(self, other):
        assert(self.length() == other.length())
        newVector = Vector([])

        for i in range(0, self.length()):
            newVector.push(self.get(i) + other.get(i))

        return newVector
    
    def subtract(self, other):
        assert(self.length() == other.length())
        newVector = Vector([])

        for i in range(0, self.length()):
            newVector.push(self.get(i) - other.get(i))

        return newVector

    def dot(self, other):
        assert(self.length() == other.length())
        total = 0

        for i in range(0, self.length()):
            total += (self.get(i) * other.get(i))

        return total
    
    def norm(self):
        total = 0
        
        for num in self.arr:
            total += num**2
        
        return total**.5
