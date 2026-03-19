def thirdmaximumnum(nums):
    nums = list(set(nums))
    nums.sort(reverse=True)
    if len(nums) >= 3:
        return nums[2]
    else:
        return nums[0]
print(thirdmaximumnum([3,2,1]))    
print(thirdmaximumnum([1,2]))       
print(thirdmaximumnum([2,2,3,1]))   