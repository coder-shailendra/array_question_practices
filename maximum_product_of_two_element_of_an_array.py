def max_product(nums):
    nums.sort()
    return (nums[-1] - 1) * (nums[-2] - 1)
print(max_product([3,4,5,2]))  
print(max_product([1,5,4,5]))   
print(max_product([3,7]))       