# # # # # # # # # # # # # # # # # # # # # # # # 
# # THIS ONE IS PRETTY SLOW
# # # # # # # # # # # # # # # # # # # # # # # # 


def find_all(sum_dig, digs):
    myList = []
    isMore = False
    for i in range(pow(10,digs)-pow(10,digs-1)):               #loop through all the numbers with the given digits
        maxDigit = 0            
        sumOfDigits = 0                                         #restart the sumofdigits
        number = i+pow(10,digs-1)                               #loop through the numbers
        if "0" in str(number):
            continue
        for l in range(digs):
            if int(str(number)[l]) >= maxDigit:
                isMore = True
            else: 
                isMore = False 
                break 
            maxDigit = int(str(number)[l])
        for j in range(digs):                         #get the sum of digits
            sumOfDigits += int(str(number)[j])          
        if sumOfDigits == sum_dig:                              #check if sum of digits is equal to given sum
            if isMore:
                myList.append(number)
    if len(myList) == 0:
        return []
        
    return [len(myList),min(myList),max(myList)]#, myList



print(find_all(22,7))

