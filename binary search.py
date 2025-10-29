def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= target:
        mid = (low + high)//2
        print(f"low={low}, high={high}, mid={mid}, nums[mid]={nums[mid]}")
    
        if nums[mid] == target:
            print(f"Found at index {mid}")
            return mid
        elif nums[mid] < target:
            print(f"→ moving right (low={low}, high={high})")
            low = mid+1
        elif nums[mid] > target:
            print(f"→ moving left (low={low}, high={high})")
            high = mid-1
    
    print(f"Not found")
    return -1
        
nums = [3, 2, 6, 9, 12, 19, 18, 21, 90, 29, 15]
print(binary_search(nums, 3))