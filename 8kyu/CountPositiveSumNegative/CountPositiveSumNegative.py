def count_positives_sum_negatives(arr):
    count = 0
    sumOfNegatives = 0
    if arr == []:
        return []
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
        else:
            sumOfNegatives += arr[i]
    return [count, sumOfNegatives]

count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])