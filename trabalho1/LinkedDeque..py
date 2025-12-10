class LinkedDeque(object):
    """Double-ended queue implementation using a doubly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = 'element', 'prev', 'next'

        def __init__(self, element, prev_node=None, next_node=None):
            self.element = element
            self.prev = prev_node
            self.next = next_node
            
    def __init__(self):
        self._head = None  
        self._tail = None  
        self._size = 0
        
    def __len__(self):
        """Returns the number of elements in the deque."""
        return self._size
    
    def _is_empty(self):
        """Returns True if the deque is empty."""
        return self._size == 0
    
    def add_first(self, e):
        """Adds element e to the front of the deque."""
        new_node = self._Node(e, None, self._head)
        
        if self._is_empty():
            self._tail = new_node  
        else:
            self._head.prev = new_node  
        
        self._head = new_node  
        self._size += 1
        
    def add_last(self, e):
        """Adds element e to the back of the deque."""
        new_node = self._Node(e, self._tail, None)
        
        if self._is_empty():
            self._head = new_node  
        else:
            self._tail.next = new_node  
        
        self._tail = new_node  
        self._size += 1
        
    def remove_first(self):
        """Removes and returns the element from the front of the deque.
        
        Raises IndexError if the deque is empty.
        """
        if self._is_empty():
            raise IndexError('Deque is empty')
        
        removed_element = self._head.element
        self._head = self._head.next  
        self._size -= 1
        
        if self._is_empty():
            self._tail = None  
        else:
            self._head.prev = None  
        
        return removed_element
    
    def remove_last(self):
        """Removes and returns the element from the back of the deque.
        
        Raises IndexError if the deque is empty.
        """
        if self._is_empty():
            raise IndexError('Deque is empty')
        
        removed_element = self._tail.element
        self._tail = self._tail.prev  
        self._size -= 1
        
        if self._is_empty():
            self._head = None  
        else:
            self._tail.next = None  
        
        return removed_element
    
    def first(self):
        """Returns (but does not remove) the element at the front of the deque.
        
        Raises IndexError if the deque is empty.
        """
        if self._is_empty():
            raise IndexError('Deque is empty')
        
        return self._head.element
    
    def last(self):
        """Returns (but does not remove) the element at the back of the deque.
        
        Raises IndexError if the deque is empty.
        """
        if self._is_empty():
            raise IndexError('Deque is empty')
        
        return self._tail.element
    
    