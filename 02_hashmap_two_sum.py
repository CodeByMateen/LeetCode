def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        val = target - num
        if val in hashmap:
            print(hashmap[val], i)
        
        hashmap[num] = i
        
nums = [2,7,2,11,15]
target = 9

twoSum(nums, target)