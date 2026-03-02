def largestPerimeter(nums):
    nums.sort()
    for i in range(len(nums) - 1, 1, -1):
        if nums[i-2] + nums[i-1] > nums[i]:
            return nums[i-2] + nums[i-1] + nums[i]
    return 0
nums = [2,1,2]
print(largestPerimeter(nums))
nums = [1,2,1,10]
print(largestPerimeter(nums))