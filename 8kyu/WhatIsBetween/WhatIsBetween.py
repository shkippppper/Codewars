def between(a,b):
    list = [a]
    i = 0
    while list[i] != b:
        list.append(list[i]+1)
        i += 1
    return list

between(-2, 2)