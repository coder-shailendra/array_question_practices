def first_repeating(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return arr[i]

    return -1


arr = [10, 5, 3, 4, 3, 5, 6]
print(first_repeating(arr))
