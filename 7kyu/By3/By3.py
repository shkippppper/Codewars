
def divisible_by_three(st): 
    sumOfSt = 0
    sum = 0
    for i in range(len(st)):
        sumOfSt = sumOfSt + int(st[i])
    while sumOfSt > sum:
        sum = sum + 3
    return True if sum == sumOfSt else False
    