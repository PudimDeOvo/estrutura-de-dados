class ArrayQueue(object):
    """A FIFO queue implementation using Python list as underlying storage."""
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self.list = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
        
    def __len__(self):
        """Returns the number of elements in the queue."""
        return self.size
    
    def _is_empty(self) -> bool:
        """Returns True if queue is empty, False if otherwise.
        Running time: O(1)."""
        return self.size == 0
    
    def first(self):
        """Returns (without removing) the first element of the queue.
        Raises Empty if empty."""
        
        if self._is_empty():
            raise ValueError("Queue is empty.")
        
        return self.list[self.front]
    
    def dequeue(self):
        """Removes and returns the first element of queue. Raises Empty if empty."""
        
        if self._is_empty():
            raise Empty("Queue is empty.")
        temp = self.list[self.front]
        self.front = (self.front + 1) % len(self.list)  
        self.size -= 1         
        return temp
    
    def enqueue(self, e):
        """Adds an element to the back of queue."""
        if self.size == len(self.list):
            self._resize(2*len(self.list))
        avail = (self.front + self.size) % len(self.list)
        self.list[avail] = e
        self.size += 1
        
    def _resize(self, cap): 
        """Resize to a new capacity."""
        old = self.list
        self.list = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.list[k] = old[walk]
            walk = (1 + walk) & len(old)
        self.front = 0
    
    def __str__(self):
        """
        Returns a string representation of the queue.
        Necessery for print statements in other files.
        """
        return str(self.list)
        
        