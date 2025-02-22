def unionElement(a, b):
    c = []  # ✅ Initialize an empty list
    i, j = 0, 0  

    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            if c and c[-1] == b[j]:  # ✅ Check if c is not empty before comparing
                j += 1
            else:
                c.append(b[j])
                j += 1    
        else:
            if c and c[-1] == a[i]:  # ✅ Check if c is not empty
                i += 1
            else:
                c.append(a[i])
                i += 1

    while i < len(a):
        if c and c[-1] == a[i]:
            i += 1
        else:
            c.append(a[i])
            i += 1

    while j < len(b):
        if c and c[-1] == b[j]:  # ✅ Ensure no duplicate elements
            j += 1
        else:
            c.append(b[j])
            j += 1

    print(c)

# Example Test Case
unionElement([2, 34, 43, 45], [43, 53, 65, 95])
