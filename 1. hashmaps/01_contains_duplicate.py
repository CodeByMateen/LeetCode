# with set

def containsDuplicate(nums):
    s = set()
    
    for num in nums:
        if num in s:
            return True
        else:
            s.add(num)
    
    return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))

# with hashmaps

def containsDuplicate(nums):
    seen = {}

    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    
    return False

nums = [1,3,4,3,2,4,2]
print(containsDuplicate(nums))