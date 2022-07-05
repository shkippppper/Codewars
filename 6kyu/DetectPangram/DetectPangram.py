import string

def is_pangram(s):
    newString = ""
    str = "".join(sorted(s.lower()))
    for i in range(len(str)):
        if str[i] not in newString:
            newString +=str[i]
    return string.ascii_letters[:26] in newString