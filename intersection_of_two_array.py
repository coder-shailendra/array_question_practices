arr1 = [1,2,4,5,3]
arr2 = [3,4,6,7,8]
intersection = []
for i in arr1:
    if i in arr2 and i not in intersection:
        intersection.append(i)
print(intersection)        