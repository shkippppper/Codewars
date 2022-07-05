

def subseq(needle, hay): 
    count = 0
    for i in range(len(needle)):
        if needle.count(needle[i]) <= hay.count(needle[i]):
            count += 1
        else: return False
    return count == len(needle) 
    



print(subseq("java", "HUUwzHpiAFdxlzHGzpAAHHnCsajUvwGkKHjJCriCFHUnqjzruoKUiyHGyfqny hAiaugcoUHkGUKHedxxAHJGACqGfnUzsFHpndAyHfFKAFresGvAuvvytaFFptgJdnhzyAkthFKAdksAsHqUeHpHdrpHcUxAfhditmlGdvHAkHHlbbvA"))