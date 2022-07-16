

def increment_string(strng):
    zeros_to_add = ""
    num_to_add = 0
    number = ""
    whilecounter = 0
    for i in range(len(strng)):
        if strng[i].isnumeric():
            number += strng[i]
        else:
            number = ""    
            

    zeros_to_add = ""
    num_to_add = 1
    print(number)
    return strng + zeros_to_add + str(num_to_add)
    


    



print(increment_string("f14oo00")) 
#increment_string("foobar099")



