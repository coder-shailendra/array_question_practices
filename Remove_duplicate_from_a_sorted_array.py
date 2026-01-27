arr = [1, 1, 2, 2, 3, 4, 4, 5, 6]

if len(arr) == 0:
    print("Empty array")
else:
    j = 0  

    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]

    print("Array after removing duplicates:")
    for k in range(j + 1):
        print(arr[k], end=" ")
