class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    #A 
    tree_a = TreeNode(1)
    tree_a.left = TreeNode(2)
    tree_a.right = TreeNode(3)

    #B
    tree_b = TreeNode(1)
    tree_b.left = TreeNode(2)
    tree_b.right = TreeNode(3)
    
    #C
    tree_c = TreeNode(1)
    tree_c.left = TreeNode(2)
    tree_c.right = TreeNode(4)

    sol = Solution()
    print(f"A e B são idênticas? {sol.isSameTree(tree_a, tree_b)}") 
    print(f"A e C são idênticas? {sol.isSameTree(tree_a, tree_c)}") 