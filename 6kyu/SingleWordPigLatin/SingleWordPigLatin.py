def pig_latin(s):
    s = s.lower()
    vowels = "aeiou"
    notInVowels = True
    if not s.isalpha(): return None
    if s[0] in vowels: return s+"way"
    for i in range(len(s)):
        
        if s[i] in vowels:
            numberToGoBack = i
            notInVowels = False
            break
    if notInVowels:
        return s+"ay"

    return s[numberToGoBack:] + s[:numberToGoBack] + "ay"


print(pig_latin("mdddp"))