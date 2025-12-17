from TreeMap import TreeMap

class RedBlackTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        def __init__(self, element, value=None, parent=None, left=None, right=None, color='RED'):
            super().__init__(element, value, parent, left, right)
            self._color = color  

    def __init__(self):
        super().__init__()

    def _set_red(self, node):
        if node: node._color = 'RED'

    def _set_black(self, node):
        if node: node._color = 'BLACK'

    def _is_red(self, node):
        return node is not None and node._color == 'RED'

    def _is_black(self, node):
        return node is None or node._color == 'BLACK'

    def _rotate(self, node):
        x = node
        y = x._parent
        z = y._parent
        
        if z is None:
            self._root = x
            x._parent = None
        else:
            if y == z._left: z._left = x
            else: z._right = x
            x._parent = z
        
        if x == y._left: 
            y._left = x._right
            if y._left: y._left._parent = y
            x._right = y
            y._parent = x
        else: 
            y._right = x._left
            if y._right: y._right._parent = y
            x._left = y
            y._parent = x

    def insert(self, key, value=None):
        if self.is_empty():
            new_node = super()._add(key, value)
            self._set_black(new_node) 
            return

        new_node = super()._add(key, value)
        
        self._rebalance_insert(new_node)

    def _rebalance_insert(self, node):
        while node != self._root and self._is_red(node._parent):
            parent = node._parent
            grandparent = parent._parent
            
            if parent == grandparent._left:
                uncle = grandparent._right
            else:
                uncle = grandparent._left
            
            if self._is_red(uncle):
                self._set_black(parent)
                self._set_black(uncle)
                self._set_red(grandparent)
                node = grandparent 
            
            else:
                if parent == grandparent._left and node == parent._right:
                    self._rotate(node) 
                    node = parent 
                    parent = node._parent 
                elif parent == grandparent._right and node == parent._left:
                    self._rotate(node) 
                    node = parent
                    parent = node._parent
                
                self._set_black(parent)
                self._set_red(grandparent)
                if parent == grandparent._left:
                    self._rotate(parent) 
                else:
                    self._rotate(parent) 
                
                break 

        self._set_black(self._root)

