# @param {Integer[]} height
# @return {Integer}
def max_area(height)
    left = 0
    right = height.length - 1
    max_area = 0
    while left < right do
        max_area = [max_area, [height[left], height[right]].min * (right - left)].max
        if height[left] < height[right]
            left += 1
        else
            right -= 1
        end
    end
    return max_area
end