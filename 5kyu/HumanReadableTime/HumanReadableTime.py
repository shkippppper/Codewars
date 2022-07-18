
def make_readable(seconds):
    SS = seconds%60
    MM = int((seconds-SS)%3600/60) 
    HH = seconds//3600
    if len(str(SS))<2: SS = "0"+str(SS)
    if len(str(MM))<2: MM = "0"+str(MM)
    if len(str(HH))<2: HH = "0"+str(HH)

    return f"{HH}:{MM}:{SS}"


print(make_readable(5))


