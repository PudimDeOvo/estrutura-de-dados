class LinkedBinaryTree:
    class _Node:
        __slots__ = 'element', 'parent', 'left', 'right'

        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element
        
        def __eq__(self, value):
            return type(value) is type(self) and value._node is self._node

    def __init__(self):
        self._root = None
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self._Node):
            raise TypeError('p must be a Node')
        if p.parent is p:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p

    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self._Node(e)
        self._size = 1
        return self._root

    def add_left(self, p, e):
        node = self._validate(p)
        if node.left is not None:
            raise ValueError('Left child exists')
        node.left = self._Node(e, parent=node)
        self._size += 1
        return node.left

    def add_right(self, p, e):
        node = self._validate(p)
        if node.right is not None:
            raise ValueError('Right child exists')
        node.right = self._Node(e, parent=node)
        self._size += 1
        return node.right

    def remove(self, p):
        node = self._validate(p)
        if node.left and node.right:
            raise ValueError('Node has two children')
        child = node.left if node.left else node.right
        if child is not None:
            child.parent = node.parent
        if node is self._root:
            self._root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self._size -= 1
        node.parent = node  
        return node.element
    
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None
    
    def _num_children(self, p):
        node = self._validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node.parent)
    
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node.left)
    
    def right(self, p): 
        node = self._validate(p)
        return self._make_position(node.right)
    
    def root(self):
        return self._make_position(self._root)
    
    def _replace(self, p, e):
        node = self._validate(p)
        old = node.element
        node.element = e
        return old
    
    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be a leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += t1._size + t2._size
        if t1._root is not None:
            t1._root.parent = node
            node.left = t1._root
            t1._root = None
            t1._size = 0
        if t2._root is not None:
            t2._root.parent = node
            node.right = t2._root
            t2._root = None
            t2._size = 0

    def _delete(self):
        def _subtree_delete(node):
            if node is not None:
                _subtree_delete(node.left)
                _subtree_delete(node.right)
                node.left = node.right = node.parent = node.element = None
                self._size -= 1
        _subtree_delete(self._root)
        self._root = None