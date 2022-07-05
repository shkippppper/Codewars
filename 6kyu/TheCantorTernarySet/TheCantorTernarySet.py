# def is_in_cantor(num, den, n):
    
#     print( False)


# is_in_cantor(1, 2, 1)

def is_in_cantor(num, den, n):
    theNumber = num/den
    if theNumber > cant()
    print(cantor(n))



def cantor(n):
    return [0] + cant(0, 1, n) + [1]

def cant(x, y, n):
    if n == 0:
        return []

    new_pts = [2*x/3 + y/3, x/3 + 2*y/3]
    return cant(x, new_pts[0], n-1) + new_pts + cant(new_pts[1], y, n-1)

cantor(10)


is_in_cantor(5, 8, 0)