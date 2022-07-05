def smash(words):
    word = ''
    for i in range(len(words)):
        word = word + words[i]+ " "
    return word[:-1]

smash(['hello', 'world', 'this', 'is', 'great'])
    