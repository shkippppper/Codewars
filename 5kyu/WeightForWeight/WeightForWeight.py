def order_weight(strng):
    splitstrng = strng.split()
    print(strng)
    sum = 0
    my_list = []
    for i in range(len(splitstrng)):
        for j in range(len(splitstrng[i])):
            sum += int(splitstrng[i][j])
        my_list.append(sum)
        print(my_list)
        sum = 0

order_weight("103 123 4444 99 2000")

# def order(strng)




0