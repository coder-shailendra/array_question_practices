def containduplicate(nums):
    if len(nums) != len(set(nums)):
        return True
    return False
print(containduplicate([1,2,3,1]))
print(containduplicate([1,2,3,4]))
