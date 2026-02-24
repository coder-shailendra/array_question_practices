def uniqueOccurrences(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    values = list(freq.values())
    return len(values) == len(set(values))
print(uniqueOccurrences([1,2,2,1,1,3]))  
print(uniqueOccurrences([1,2]))           
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))  