class TreeMap:
    class _Node:
        __slots__ = '_element', '_value', '_parent', '_left', '_right'
        def __init__(self, element, value=None, parent=None, left=None, right=None):
            self._element = element  
            self._value = value      
            self._parent = parent
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None 
        self._size = 0

    def is_root(self, node):
        return self._root == node

    def _add(self, key, value=None):
        if self._root is None:
            self._root = self._Node(key, value)
            self._size += 1
            return self._root
        
        node = self._root
        while True:
            if key < node._element:
                if node._left is None:
                    node._left = self._Node(key, value, node)
                    self._size += 1
                    return node._left
                node = node._left
            elif key > node._element:
                if node._right is None:
                    node._right = self._Node(key, value, node)
                    self._size += 1
                    return node._right
                node = node._right
            else:
                node._value = value
                return node

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size