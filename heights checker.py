def height_cheaker(heights):
    expected = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i]!= expected[i]:
            count +=1
    return count
heights = [1,2,3,4,5]
print(height_cheaker(heights))
heights = [2,4,1,6,3]
print(height_cheaker(heights))