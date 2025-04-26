# Problem: sort the letter on the basis of occurance of the of character.

# how to sort the dictionary

dictionary = {"c":2,"d":5,"a":1}
print(dictionary.items())           #convert into list of tuples
sort = sorted(dictionary.items(),key=lambda x:x[1],reverse=True) 
print(sort)     

# how to work with the sorted list of tuples [("c":2,"d":5)]
for char,count in sort:
    print(char,count)

def sortString(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    sort = sorted(freq.items(),key = lambda x:x[1],reverse = True)

    return "".join(char*count for char,count in sort)            

print(sortString("stree"))


