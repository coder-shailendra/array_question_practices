arr = [3, 1, 2, 4, 2, 1, 5, 6, 4]

seen = set()
result = []

for x in arr:
    if x not in seen:
        seen.add(x)
        result.append(x)

print("Array after removing duplicates:")
for i in result:
    print(i, end=" ")
