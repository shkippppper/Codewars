def dig_pow(n, p):
    product = 0
    for i in range(len(str(n))):
        product += pow(int(str(n)[i]),p+i)
    if product%n ==0:
        return product//n
    else: return -1

