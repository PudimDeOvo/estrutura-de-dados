def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def order_vector(nums):
    for num in nums:
        if is_even(num):
            nums.remove(num)
            nums.insert(0, num)
            continue
    print(nums)

print("running")
order_vector([3,1,2,4])
print("ran")