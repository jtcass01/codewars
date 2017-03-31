class matrix:
    def __init__(self, arr=[]):
        self.arr = arr

    def __str__(self):
        string = "["

        for line in self.arr:
            string += "["
            for value in line:
                string += str(value) + ","
            string = string[:-1] + "]\n"
        string = string[:-1] + "]"

        return string

    def getDeterminant(self):
        result = 0
        
        if(len(self.arr) == 1):
            return self.arr[0][0]
        elif(len(self.arr) == 2):
            return self.arr[0][0]*self.arr[1][1] - self.arr[0][1] * self.arr[1][0]
        else:
            return self._getDeterminant(self.arr)

    def _getDeterminant(self, arr):
        result = 0
        
        if(len(arr) == 2):
            result = arr[0][0]*arr[1][1] - arr[0][1]*arr[1][0]
        else:
            for i in range(0, len(arr)):
                if(i%2==0):
                    result += arr[0][i]*self._getDeterminant(self._getIntermediate(arr, i))
                else:
                    result -= arr[0][i]*self._getDeterminant(self._getIntermediate(arr, i))
        return result

    def getIntermediate(self, x):
        intermediate = []
        line = []
        for arr_i in range(0, len(self.arr)):
            if(arr_i > 0):
                for value_i in range(0,len(self.arr[arr_i])):
                    if(value_i != x):
                        line.append(self.arr[arr_i][value_i])
                intermediate.append(line)
                line = []
        return intermediate

    def _getIntermediate(self, arr, x):
        intermediate = []
        line = []
        for arr_i in range(0, len(arr)):
            if(arr_i > 0):
                for value_i in range(0,len(arr[arr_i])):
                    if(value_i != x):
                        line.append(arr[arr_i][value_i])
                intermediate.append(line)
                line = []
        return intermediate        
      
                        
def determinant(given):
    m = matrix(given)
    return m.getDeterminant()
