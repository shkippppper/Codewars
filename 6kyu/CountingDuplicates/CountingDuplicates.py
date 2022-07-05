import time

time.sleep(1)
def duplicate_count(text):
    text = text.lower()
    counter = 0
    texto = ""
    for i in range(len(text)):
        if text.count(text[i])>1:
            if text[i] not in texto:
                texto += text[i]
                counter +=1
    return counter



print(duplicate_count("abcdeaB"))