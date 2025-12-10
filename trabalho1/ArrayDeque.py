import ArrayQueue

class ArrayDeque(ArrayQueue):
    """Queue-like data type that supports deletion and insertions from both ends (front and end)."""
    
    def __init__(self):
        self.list = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
        self.last = DEFAULT_CAPACITY
    
    def last(self):
        """Returns (without removing) the last element of the queue.
        Raises Empty if empty."""
        
        if self.is_empty():
            raise Empty("Queue is empty.")
        
        return self.list[self.last]
    
    def add_first(self):
        """Adds an element to the front of queue."""
        if self.size == len(self.list):
            self.resize(2*len(self.list))
        avail = (self.last + self.size) % len(self.list)
        self.data[avail] = e
        self.size += 1
        
    def delete_last(self):
        """Deletes last element of queue."""
        
        if self.is_empty():
            raise Empty("Queue is empty.")
        temp = self.list[self.last]
        self.last = self.last + 1 % len(self.list)  
        self.size -= 1         
        return temp