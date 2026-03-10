def twoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]

        if s == target:
            print(left, right)
            return
        elif s < target:
            left +=1
        else:
            right -=1

twoSum([1,2,3,4,6], 6)