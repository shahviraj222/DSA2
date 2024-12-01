def cache(func):
    cache_value = {}
    def wrapper(*arg):
        if arg in cache_value:
            print("Value From Catch : ",cache_value[arg])
            return cache_value[arg]
        result = func(*arg)
        cache_value[arg] = result
        print("Function called Value is : ",result)
        return result
    return wrapper

@cache
def mutliply(x,y):
    return x*y

mutliply(4,3)
mutliply(6,3)
mutliply(2,3)
mutliply(4,3)