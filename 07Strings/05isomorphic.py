# isomorphic means one to one mapping only.
# age = add  return false g and e not map to same element

# 1 How to check the values in dictionary 
a = {"name":"viraj","surname":"shah"}
if "viraj" in a.values():
    print("this way we can check dictionary values")


def isomorphic(s,t):
    if len(s) != len(t):
        return False
    
    s_to_t ={}
    tmapped = set()
    
    for i in range(len(s)):
        sc = s[i]
        tc = t[i]
        if sc in s_to_t:
            if s_to_t[sc] != tc:
                return False
        else:
            if tc in tmapped:
                return False
            s_to_t[sc] = tc
            tmapped.add(tc)
    return True

            

