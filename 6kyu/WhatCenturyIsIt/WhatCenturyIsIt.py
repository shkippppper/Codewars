
def centuryDec(year):
    century = 0
    b=str(year)[0:2]
    if int(year)-int(b)*100!=0:
        century = int(b)+1
        return century
    else:
        century = b
        return century

def centuryPrefix(year):
    century = centuryDec(year)
    prefix = ""
    if int(century) == 11:
        prefix = "st"
    elif int(century) == 12:
        prefix = "nd"
    elif int(century) == 13:
        prefix = "rd"
            
    elif int(century)%10==1:
        prefix = "st"
    elif int(century)%10==2:
        prefix = "nd"
    elif int(century)%10==3:
        prefix = "rd"

    else:
        prefix = "th"
    return prefix

def what_century(year):
    
    print(str(centuryDec(year))+centuryPrefix(year))
    
what_century("7100")