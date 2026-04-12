# here we have source helper and destination as 3 road
# n is disk number
# here x,y are used for counting how many moves we have to make.

def hanio(n,source,helper,destination):
    if n == 0:
        return 0
    if n == 1:
        print(f"move {n} from {source} to {destination}")
        return 1
    
    x = hanio(n-1,source,destination,helper)
    print(f"move {n} from {source} to {destination}")
    y = hanio(n-1,helper,source,destination)
    return x+y+1


count = hanio(3,"a","b","c")
print(count)