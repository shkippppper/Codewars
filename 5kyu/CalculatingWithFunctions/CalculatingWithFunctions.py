
def zero(symbol="",secondNumber=0): 
    if symbol != "":
        return calculate(0,symbol[0],int(symbol[1:]))
    else:
        return secondNumber

def one(symbol="",secondNumber=1):
    if symbol != "":
        return calculate(1,symbol[0],int(symbol[1:]))    
    else:
        return secondNumber

def two(symbol="",secondNumber=2): 
    if symbol != "":
        return calculate(2,symbol[0],int(symbol[1:]))
    else:
        return secondNumber

def three(symbol="",secondNumber=3):
    if symbol != "":
        return calculate(3,symbol[0],int(symbol[1:]))    
    else:
        return secondNumber

def four(symbol="",secondNumber=4): 
    if symbol != "":
        return calculate(4,symbol[0],int(symbol[1:]))
    else:
        return secondNumber

def five(symbol="",secondNumber=5):
    if symbol != "":
        return calculate(5,symbol[0],int(symbol[1:]))    
    else:
        return secondNumber

def six(symbol="",secondNumber=6): 
    if symbol != "":
        return calculate(6,symbol[0],int(symbol[1:]))
    else:
        return secondNumber

def seven(symbol="",secondNumber=7):
    if symbol != "":
        return calculate(7,symbol[0],int(symbol[1:]))    
    else:
        return secondNumber

def eight(symbol="",secondNumber=8): 
    if symbol != "":
        return calculate(8,symbol[0],int(symbol[1:]))
    else:
        return secondNumber

def nine(symbol="",secondNumber=9):
    if symbol != "":
        return calculate(9,symbol[0],int(symbol[1:]))    
    else:
        return secondNumber

def plus(Number): 
    return "+" + str(Number)
def minus(Number):
    return "-" + str(Number)
def times(Number): 
    return "*" + str(Number)
def divided_by(Number): 
    return "/" + str(Number)


def calculate(fn,op,sn):
    if op == "+":
        return fn+sn
    elif op == "-":
        return fn-sn
    elif op == "*":
        return fn*sn
    elif op == "/":
        return fn//sn




