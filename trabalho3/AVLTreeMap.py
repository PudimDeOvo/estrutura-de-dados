from TreeMap import TreeMap

class AVLTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        __slots__ = '_height'
        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0
            
        def left_height(self):
            return self._left._height if self._left is not None else 0
        
        def right_height(self):
            return self._right._height if self._right is not None else 0

    def _recompute_height(self, node):
        node._height = 1 + max(node.left_height(), node.right_height())
        
    def _is_balanced(self, node):
        return abs(node.left_height() - node.right_height()) <= 1
    
    def _taller_child(self, node):
        if node.left_height() > node.right_height():
            return node._left
        elif node.left_height() < node.right_height():
            return node._right
        else:
            if self.is_root(node): return node._left
            if node == node._parent._left: return node._left
            else: return node._right

    def _rotate(self, p):
        x = p
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)
        
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    def _relink(self, parent, child, make_left_child):
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _restructure(self, x):
        y = x._parent
        z = y._parent
        if (x == y._left) == (y == z._left): 
            self._rotate(y)
            return y
        else: 
            self._rotate(x)
            self._rotate(x)
            return x

    def _rebalance(self, node):
        while node is not None:
            old_height = node._height
            if not self._is_balanced(node):
                node = self._restructure(self._taller_child(self._taller_child(node)))
                self._recompute_height(node._left)
                self._recompute_height(node._right)
            self._recompute_height(node)
            if node._height == old_height and node is not None and self._is_balanced(node):
                node = node._parent 
            else:
                node = node._parent

    def insert(self, element):
        node = self._add(element)
        self._rebalance(node)     

    def delete(self, element):
        node = self._root
        while node and node._element != element:
            if element < node._element: node = node._left
            else: node = node._right
        
        if not node: return 
        
        if node._left and node._right:
            successor = node._right
            while successor._left: successor = successor._left
            node._element = successor._element
            node = successor 
        
        child = node._left if node._left else node._right
        parent = node._parent
        
        if child: child._parent = parent
        
        if parent is None: self._root = child
        elif node == parent._left: parent._left = child
        else: parent._right = child
        
        self._rebalance(parent)