def perimeter(n):
    fibs = []
    fibs.append(0)
    fibs.append(1)

    for i in range(0, n):
        fibs.append(fibs[i] + fibs[i+1])
        
    return 4 * sum(fibs)
    
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def sum(arr):
    result = 0
    
    for val in arr:
        result += val
        
    return result
