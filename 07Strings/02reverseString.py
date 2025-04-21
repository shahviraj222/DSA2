# problem: Reverse the string and remove the extra spaces between them

#1 how to strip in python
s = "viraj        "
trimed = s.strip()
trimed = s.lstrip()    # only remove front white space
trimed = s.rstrip()    # only remove back white space

#2 how to convert list into string
s = ["one","two","three"]
s = " ".join(s)       

#3 how to reverse a list
a = ["one","two","three"]
a.reverse()

    
def reverse(s):
    trimed = s.strip()
    result = []
    rand = ""
    for char in trimed:
        if char == " ":
            if rand == "":
                continue
            result.append(rand)
            rand = ""
        rand+=char    

    result.append(rand)              # this is for the last word
    result.reverse()

    return " ".join(result)

print(reverse("  hello world  ") )           


