# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        q = deque([root])

        def findHeight(root) -> int:
            if not root:
                return 0
            
            return 1 + max(findHeight(root.left), findHeight(root.right))

        while q:
            node = q.pop()
            left_height = findHeight(node.left)
            right_height = findHeight(node.right)

            if abs(left_height - right_height) > 1:
                return False
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return True