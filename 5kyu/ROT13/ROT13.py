def rot13(message):
    normal =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    changed = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    newlist=list(message)
    for i in range(len(message)):
        if message[i] in normal:
            a = normal.index(message[i])
            newlist[i] = changed[a]
    return "".join(newlist)

rot13("EBG13 rknzcyr.")


