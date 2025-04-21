# Problem: Find the longest common prefix form the list

# there is problem in the code not run for the ["aa","aa"]
def longestPrefix(s):
    a = {}
    result = []
    for char in s[0]:
        a[char] = 1

    for i in range(1,len(s)):
        for char in s[i]:
            if char in a:
                a[char]+=1

    for char in s[0]:
        if a[char] == len(s):
                 result.append(char)

    return "".join(result)    

print(longestPrefix(["flower", "flow", "flight"]))             