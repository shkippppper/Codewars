from random import randint



def shuffled_deck():
    suits = ["H","C","D","S"]
    empty_list = []
    counter = 1
    while len(empty_list) !=52:
        symbol = suits[randint(0,3)]
        card = symbol+" "+str(randint(1,13))
        if card in empty_list:
            counter += 1
        else:
            empty_list.append(card)
        #print(empty_list)
    return(empty_list)
        