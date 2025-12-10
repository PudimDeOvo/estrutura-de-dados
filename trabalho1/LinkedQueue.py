class LinkedQueue(object):
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = 'element', 'next'

        def __init__(self, element, next_node=None):
            self.element = element
            self.next = next_node
            
    def __init__(self):
        self._head = None  
        self._tail = None  
        self._size = 0
        
    def __len__(self):
        """Returns the number of elements in the queue."""
        return self._size
    
    def _is_empty(self):
        """Returns True if the queue is empty."""
        return self._size == 0
    
    def enqueue(self, e):
        """Adds element e to the back of the queue."""
        new_node = self._Node(e)
        
        if self._is_empty():
            self._head = new_node  
        else:
            self._tail.next = new_node  
        
        self._tail = new_node  
        self._size += 1
        
    def dequeue(self):
        """Removes and returns the element from the front of the queue.
        
        Raises IndexError if the queue is empty.
        """
        if self._is_empty():
            raise IndexError('Queue is empty')
        
        dequeued_element = self._head.element
        self._head = self._head.next  
        self._size -= 1
        
        if self._is_empty():
            self._tail = None  
        
        return dequeued_element
    
    def first(self):
        """Returns (but does not remove) the element at the front of the queue.
        
        Raises IndexError if the queue is empty.
        """
        if self._is_empty():
            raise IndexError('Queue is empty')
        
        return self._head.element
    
    
    