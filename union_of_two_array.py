arr1 = [1,2,3,4,5,6]
arr2 = [7,8,9,6,5,4]
union = []
for i in arr1:
    if i not in union:
        union.append(i)
for i in arr2:
    if i not in union:
        union.append(i)        
print(union)        