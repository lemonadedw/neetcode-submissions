# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def contains(self, r, t):
            if not r:
                return False
            
            if r.val  == t.val:
                return True
            
            return self.contains(r.right, t) or self.contains(r.left, t)
            
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
        elif (self.contains(root.left, p) and self.contains(root.right, q)) or (self.contains(root.right, p) and self.contains(root.left, q)):
            return root
        elif self.contains(root.left, p) and self.contains(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)