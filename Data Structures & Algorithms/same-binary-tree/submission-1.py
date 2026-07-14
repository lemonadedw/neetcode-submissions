# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.s1, self.s2 = [], []

        def dfs(root, s):
            if not root:
                s.append(None)
                return
            
            s.append(root.val)
            dfs(root.left, s)
            dfs(root.right, s)
        
        dfs(p, self.s1)
        dfs(q, self.s2)

        if len(self.s1) != len(self.s2): return False

        for i in range(len(self.s1)):
            if self.s1[i] != self.s2[i]:
                return False
        
        return True






        
        