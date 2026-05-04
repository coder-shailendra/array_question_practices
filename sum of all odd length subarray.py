def lengthofsubarray(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        total = (i + 1) * (n - i)
        odd_count = (total + 1) // 2
        total_sum += arr[i] * odd_count
    return total_sum
print(lengthofsubarray([1,4,2,5,3]))  
print(lengthofsubarray([1,2]))       
print(lengthofsubarray([10,11,12]))   