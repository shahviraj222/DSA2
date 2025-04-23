# problem: find weather the rotated string is == goal or not


def FindroatedString(s,goal):
    if len(s) != len(goal):
        return False
    for i in range(1,len(s)+1):
        result = s[i:]+s[:i]
        if result == goal:
            return True
    return False

# here s+s doing concatenate 
# s+s contain all the rotation.
# in operator checking for weatehr the goal substring is there in s+s or not.
def FindroatedString(s,goal)->bool:
    if len(s) != len(goal):
        return False
    return goal in (s+s)   