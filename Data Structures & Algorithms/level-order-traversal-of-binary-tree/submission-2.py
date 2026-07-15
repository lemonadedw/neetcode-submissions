# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        layer = [] # list of int
        result = [] # list of list of int

        level_size = len(q)

        while q:
            for i in range(level_size):
                node = q.popleft()
                layer.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(layer.copy())
            layer = []
            level_size = len(q)
        
        return result
