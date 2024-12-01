# frequnecy count of numbers

arr = [23,34,45,23,23,54,34,9,2,2,2,10]
def frequency_count(arr):
    map = {}
    for i in range(0,len(arr)):
        if arr[i] in map:
            map[arr[i]] +=1
            continue
        map[arr[i]] = 1

    for k,v in map.items():
        print(f"{k}:{v}")
    
    return map

'''
#here problem is we getting only key not pair 

def maximum_frequency(map:dict):
    return max(map.values())

def minimum_frequency(map:dict):
    return min(map.values()) 

max(map)
here max only compare the keys and return also key  ʔ„
'''

def maximum_frequency(map:dict):
    map_key = max(map,key = map.get )  # key arugment take function and apply it before comparison of the value (here vlaue is key) map.get(key) this is what happens
    return (map_key,map[map_key])

def minimum_frequency(map:dict):
    map_key = min(map,key = map.get)
    return (map_key,map[map_key])  

map = frequency_count(arr)
print(maximum_frequency(map))  
print(minimum_frequency(map))      
