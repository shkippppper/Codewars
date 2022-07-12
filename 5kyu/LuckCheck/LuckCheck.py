def luck_check(string):
    if string.isnumeric():    
            length = len(string)//2
            leftside = 0
            rightside = 0
            for i in range(len(string)//2):
                leftside += int(string[i])  
            for j in range(len(string)//2):
                rightside += int(string[-length+j])
            return rightside == leftside
    else:
        raise TypeError("nope nope")
    


