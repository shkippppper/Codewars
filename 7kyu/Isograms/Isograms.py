def is_isogram(string):
    a = ""
    for i in range(len(string)):
        if string.upper()[i] in a:
            return False
        else:
            a += string.upper()[i]
    return True


print(is_isogram("Dermatoglyphiccs"))





