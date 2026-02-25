def containnearbyduplicate(nums,k):
    last_index = {}
    for i in range(len(nums)):
        if nums[i] in last_index:
            if i - last_index[nums[i]] <= k:
                return True
        last_index[nums[i]] = i
    return False
print(containnearbyduplicate([1,2,3,1],3))
print(containnearbyduplicate([1,0,1,1],1))
print(containnearbyduplicate([1,2,3,1,2,3],2))
       