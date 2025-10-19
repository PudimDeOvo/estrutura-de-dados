def has_dupe(nums):
    first_index = 0
    size = len(nums)
    while first_index < size:
        second_index = first_index + 1
        while second_index < size:
            if nums[first_index] == nums[second_index]:
                print("true")
                return
            second_index += 1
        first_index += 1
    print("false")
    return 
        
has_dupe([1,2,3,1])
has_dupe([1,2,3,4])
has_dupe([1,1,1,3,3,4,3,2,4,2])