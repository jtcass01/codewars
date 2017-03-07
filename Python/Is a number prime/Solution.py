def is_prime(num):
    if(num < 0):
        num*=-1
    if(num == 0 or num == 1):
        return False
    else:
        for i in range(2,10):
            if(num!=i):
                if (num%i == 0):
                    return False
        return True
