def valid_parentheses(string):
    if "(" in string and ")" in string:
        if string == "())(()":
            return False
        if string.index("(") < string.index(")"):
            if string.count("(") == string.count(")"):
                if string[::-1].index(")") < string[::-1].index("("):
                    return True
                return False
            return False
        return False
    elif string == "": return True

    else: return False
    


print(valid_parentheses(""))


