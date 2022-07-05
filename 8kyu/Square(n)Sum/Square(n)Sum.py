def square_sum(numbers):
    numberToDisplay = 0
    for i in range(len(numbers)):
        numberToDisplay += numbers[i]**2
    return numberToDisplay

square_sum([0, 3, 4, 5])