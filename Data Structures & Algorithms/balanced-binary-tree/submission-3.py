# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])

        def findHeight(root) -> int:
            if not root:
                return 0
            
            return 1 + max(findHeight(root.left), findHeight(root.right))

        while q:
            node = q.pop()
            if not node:
                continue

            if abs(findHeight(node.left) - findHeight(node.right)) > 1:
                return False
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return True