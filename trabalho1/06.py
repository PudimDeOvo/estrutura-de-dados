import ArrayQueue

def _operations_on_queue(queue):
    result = (
        queue.enqueue(5), 
        queue.enqueue(3), 
        queue.dequeue(),
        queue.enqueue(2),
        queue.enqueue(8),
        queue.dequeue(),
        queue.dequeue(),
        queue.enqueue(9),
        queue.enqueue(1),
        queue.dequeue(),
        queue.enqueue(7),
        queue.enqueue(6),
        queue.dequeue(),
        queue.dequeue(),
        queue.enqueue(4),
        queue.dequeue(),
        queue.dequeue())
    
    return result

queue = ArrayQueue.ArrayQueue() 
final_result = _operations_on_queue(queue)

print(final_result)