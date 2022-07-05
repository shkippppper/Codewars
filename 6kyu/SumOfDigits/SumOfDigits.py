def digital_root(n):
    n = str(n)
    while len(n) >1:
        answer = 0
        for x in range(len(n)):      
            newList = n
            numberFromList = int(newList[x])           
            answer = answer + numberFromList
            print(answer)
        n = str(answer)
    return(int(n)) 