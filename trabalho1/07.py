import ArrayDeque

def _operations_on_deque(deque):
    result = (
        deque.add_first(4), 
        deque.add_last(8), 
        deque.add_last(9), 
        deque.add_first(5), 
        deque.last(),
        deque.delete_first( ), 
        deque.delete_last( ), 
        deque.add_last(7), 
        deque.first( ), 
        deque.last( ), 
        deque.add_last(6), 
        deque.delete_first( ), 
        deque.delete_first( ))
    
    return result

deque = ArrayDeque.ArrayDeque() 
final_result = _operations_on_deque(deque)

print(final_result)