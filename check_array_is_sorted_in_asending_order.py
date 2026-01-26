arr = [10, 20, 30, 40, 50]

sorted_arr = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted_arr = False
        break

if sorted_arr:
    print("Array is sorted in ascending order")
else:
    print("Array is NOT sorted")
