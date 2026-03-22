def shufflearray(nums,n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result
nums = [2,5,1,3,4,7]
n = 3
print(shufflearray(nums, n))
nums = [1,2,3,4,4,3,2,1]
n = 4
print(shufflearray(nums, n))   
nums = [1,1,2,2]
n = 2
print(shufflearray(nums, n))  