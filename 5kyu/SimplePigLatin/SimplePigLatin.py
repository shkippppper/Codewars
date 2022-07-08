from string import punctuation

def pig_it(text):
    newText = text.split(" ")
    for i in newText:
        for j in range(len(i)):
            if i[j] in punctuation:
                punct = i[j]
            else: newText[i] = newText[i]+"ay"
        
        #else: newText[i] = newText[i]

    return newText

print(pig_it('Pig, latin is cool'))