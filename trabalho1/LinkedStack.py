class LinkedStack(object):
    """LIFO Stack implementation using a singly linked list for storage."""

    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = 'element', 'next'

        def __init__(self, element, next_node=None):
            self.element = element
            self.next = next_node
    
    def __init__(self):
        self._head = None 
        self._size = 0

    def __len__(self):
        """Returns the number of elements in the stack."""
        return self._size

    def _is_empty(self):
        """Returns True if the stack is empty."""
        return self._size == 0
    
    def push(self, e):
        """Adds element e to the top of the stack."""
        new_node = Node(e, self._head) 
        
        self._head = new_node
        
        self._size += 1
        
    def pop(self):
        """Removes and returns the element from the top of the stack.
        
        Raises IndexError if the stack is empty.
        """
        if self._is_empty():
            raise IndexError('Stack is empty')
        
        popped_element = self._head.element
        self._head = self._head.next  
        self._size -= 1
        
        return popped_element
    
    def peek(self):
        """Returns (but does not remove) the element at the top of the stack.
        
        Raises IndexError if the stack is empty.
        """
        if self._is_empty():
            raise IndexError('Stack is empty')
        
        return self._head.element