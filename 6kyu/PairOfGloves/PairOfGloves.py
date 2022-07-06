def number_of_pairs(gloves):
    newDict = {}
    sum = 0
    for i in range(len(gloves)):
        if gloves[i] not in newDict:
            newDict.update({gloves[i]:0})
    for i in newDict:
        appearances = gloves.count(i)
        pairs = appearances//2
        newDict.update({i:pairs})
    for i in range(len(newDict.values())):
        sum += list(newDict.values())[i]
    return sum
    
    
    
