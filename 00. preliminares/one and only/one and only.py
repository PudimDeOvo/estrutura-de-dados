def one_and_only(nums):
    size = len(nums)
    first_index = 0
    while first_index < size: 
        second_index = 0
        seen = 0
        while second_index < size:
            if nums[first_index] == nums[second_index]:
                seen += 1
            second_index += 1
        
        if seen == 1:
            print(f"{nums[first_index]}")
            return nums[first_index]
        
        first_index += 1    

print("running")
one_and_only([2,2,1])
one_and_only([4,1,2,1,2])
one_and_only([1])
