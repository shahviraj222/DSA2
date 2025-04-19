# problem : remove outermost parenthis 
def removeParenthesis(string):
    count = 0
    result = []
    for char in string:
        if char == "(":
            if count>0:
                result.append(char)
            count+=1

        if char ==")":
            count-=1
            if count>0:
                result.append(char)

    return "".join(result)

print(removeParenthesis("(()())(())"))             

