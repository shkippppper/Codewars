def joker_card(joker_nums, ticket_serials):
    joker = ""
    placing = 0
    final_result = [0,0,0]
    winnings = ["Losing card","Losing card","V type","IV type","III type","II type","I type"]
    for i in range(len(joker_nums)):
        joker = joker + str(joker_nums[i])[-1]

    for j in range(len(ticket_serials)):
        for k in range(len(ticket_serials[j])):
            if ticket_serials[j][-1-k:] == joker[-1-k:]:
                 placing = placing + 1
        final_result[j] = winnings[placing]
        placing = 0  
    
    return final_result