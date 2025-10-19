def two_sums(nums, target):
    size = len(nums)
    first_index = 0
    
    while first_index < size:
        second_index = first_index + 1
        while second_index < size:
            if nums[first_index] + nums[second_index] == target:
                print(f"index: {[first_index]} and {[second_index]}")
                return
            second_index += 1
        first_index += 1
    
print("running")
two_sums([2,7,11,15], 9)
print("running")
two_sums([3, 2, 4], 6)
print("running")
two_sums([3, 3], 6)