


def move_zeros(array):
    rangeToGo = array.count(0)
    for i in range(rangeToGo):
        array.remove(0)
    for i in range(rangeToGo):
        array.append(0)
    return (array)
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))



