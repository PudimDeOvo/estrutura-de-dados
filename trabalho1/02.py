import ArrayStack

def _operations_on_stack(stack):
    result = (
        stack.push(5), 
        stack.push(3), 
        stack.pop(),
        stack.push(2),
        stack.push(8),
        stack.pop(),
        stack.pop(),
        stack.push(9),
        stack.push(1),
        stack.pop(),
        stack.push(7),
        stack.push(6),
        stack.pop(),
        stack.pop(),
        stack.push(4),
        stack.pop(),
        stack.pop())
    
    return result

my_stack = ArrayStack.ArrayStack() 
final_result_tuple = _operations_on_stack(my_stack)

print(final_result_tuple)