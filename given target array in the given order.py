def createtargetarray(nums,index):
    target = []
    for i in range(len(nums)):
        target.insert(index[i],nums[i])
    return target
print(createtargetarray([0,1,2,3,4], [0,1,2,2,1]))
print(createtargetarray([1,2,3,4,0], [0,1,2,3,0]))
print(createtargetarray([1], [0]))
