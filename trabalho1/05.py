import ArrayStack
# Demonstration of recursive_empty method
S = ArrayStack.ArrayStack()
S.push(1)
S.push(2)
S.push(3)
print(f"Stack before: {S.__str__()}")  
S.recursive_empty()
print(f"Stack after: {S.__str__()}") 

# actual reversal function asked in question 5
def reverse_list_with_stack(data_list):
    """Reverses the elements of a list in-place using a stack."""
    
    S = ArrayStack.ArrayStack() 
    
    for item in data_list:
        S.push(item)
        print(f"pushed {item}. Stack: {S}")
    
    index = 0
    while not S.is_empty():
        item = S.pop() 
        
        data_list[index] = item
        
        index += 1
        print(f"popped {item}. List: {data_list}")
        
    print("done")


list = [10, 20, 30, 40, 50]

print(f"original List: {list}")
reverse_list_with_stack(list)
print(f"final Reversed List: {list}")  