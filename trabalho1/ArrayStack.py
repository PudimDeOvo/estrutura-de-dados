class ArrayStack(object):
    """A LIFO stack implementation using Python list as underlying storage"""
    def __init__(self, iterable = None):
        """Initializes the stack."""
        self.list = []
    
    def len(self):
        """Returns the number of elements of the stack.
        Running time: O(1)."""
        return len(self.list)
    
    def is_empty(self):
        """Returns True if stack is empty, False if otherwise.
        Running time: O(1)."""
        
        return bool(len(self.list) == 0)
    
    def push(self, item):
        """Inserts an item at the top of the stack
        Running time: O(1)."""
        
        return self.list.append(item)
        
    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        Running time: O(1)."""
        last_item_index = len(self.list) - 1
        if last_item_index < 0:
            return None
        else:
            return self.list[last_item_index]
        
    def pop(self):
        """Removes an item from the top of the stack and
        returns it. An error occurs if the stack is empty.
        Running time: O(1)."""
        if self.peek is None:
            return ValueError("List is empty")
        else:
            return self.list.pop()
        
    def __str__(self):
        """
        Returns a string representation of the stack.
        Necessery for print statements in other files.
        """
        return str(self.list)
    
    def recursive_empty(self):
        """
        Recursively removes all elements from the stack.
        
        This method demonstrates how stack operations can be done recursively.
        """
        
        if self.is_empty():
            return
        
        self.pop() 
        
        self.recursive_empty()