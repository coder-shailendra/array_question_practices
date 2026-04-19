def max_candy_types(candyType):
    unique_types = len(set(candyType))  
    n = len(candyType)
    return min(unique_types, n // 2)
print(max_candy_types([1,1,2,2,3,3]))  
print(max_candy_types([1,1,2,3]))      