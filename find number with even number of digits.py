def findnumbers(nums):
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count
nums = [12,345,2,6,7896]
print(findnumbers(nums))
nums = [12,345,7896,886891,72,4321]
print(findnumbers(nums))
