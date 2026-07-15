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
        count = 0

        while q:
            node = q.popleft()
            layer.append(node.val)

            count += 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            if count == level_size:
                result.append(layer.copy())
                layer = []
                count = 0
                level_size = len(q)

                
        
        return result
