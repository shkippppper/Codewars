def hotpo(n):
    result = 0
    while n !=1:
        if n%2 != 0:
            n = n*3 + 1
        else:    
            n /= 2
        result += 1
    return result

hotpo(23)