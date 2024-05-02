# url: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/


def canBeIncreasing(nums: list):
    copy_nums = nums.copy() 
    for i in range(len(nums) - 1):  
        if nums[i] >= nums[i + 1]:
            nums.pop(i)
            break
    if nums == sorted(set(nums)):  
        return True
    
    for j in range(len(copy_nums) - 1, 0, -1):  
        if copy_nums[j] <= copy_nums[j - 1]:
            copy_nums.pop(j)
            break
    if copy_nums == sorted(set(copy_nums)):
        return True
    return False


print(canBeIncreasing([1, 2, 10, 5, 7]))
print(canBeIncreasing([2, 3, 1, 2]))
print(canBeIncreasing([1, 1, 1]))
print(canBeIncreasing([1, 1]))
print(canBeIncreasing([100, 21, 100]))
