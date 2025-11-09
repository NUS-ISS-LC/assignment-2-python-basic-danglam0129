def find(nums, target):
# write your implementation here
    nums_dictionary = {}

    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in nums_dictionary:
            return [i, nums_dictionary[difference]]
        
        nums_dictionary[nums[i]] = i

    return None


print(find([2,7,11,15], 9))
print(find([3,2,4], 6))