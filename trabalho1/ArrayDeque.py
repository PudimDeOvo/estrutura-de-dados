from ArrayQueue import ArrayQueue 

class ArrayDeque(ArrayQueue):
    """Queue-like data type that supports deletion and insertions from both ends (front and end)."""
    
    def __init__(self):
        super().__init__()
    
    def last(self):
        """Returns (without removing) the last element of the queue.
        Raises Empty if empty."""
        
        if self._is_empty():
            raise Empty("Deque is empty.")
        rear = (self.front + self.size - 1) % len(self.list)
        return self.list[rear]
    
    def add_last(self, e):
        """Adds an element to the back (rear) of the deque."""
        
        if self.size == len(self.list):
            self._resize(2 * len(self.list))
            
        avail = (self.front + self.size) % len(self.list)
        
        self.list[avail] = e
        self.size += 1
    
    def add_first(self, e):
        """Adds an element to the front of queue."""
        if self.size == len(self.list):
            self._resize(2 * len(self.list))
            
        self.front = (self.front - 1) % len(self.list)
        
        self.list[self.front] = e
        self.size += 1
        
    def delete_first(self):
        """
        Removes and returns the element at the front of the deque.
        This operation is equivalent to the parent class's dequeue().
        """
        return self.dequeue()
        
    def delete_last(self):
        """Deletes last element of queue."""
        
        if self._is_empty():
            raise Empty("Deque is empty.")
            
        rear = (self.front + self.size - 1) % len(self.list)
        
        element = self.list[rear]
        self.list[rear] = None
        
        self.size -= 1
        return element
    
    def __str__(self):
        """
        Returns a string representation of the deque.
        Necessery for print statements in other files.
        """
        return str(self.list)
        