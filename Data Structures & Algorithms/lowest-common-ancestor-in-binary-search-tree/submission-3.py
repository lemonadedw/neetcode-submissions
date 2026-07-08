# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findPath(self, root: TreeNode, node: TreeNode, path: List[TreeNode]) -> List[TreeNode]:
        path.append(root)

        if node.val == root.val:
            return path
        elif node.val > root.val:
            return self.findPath(root.right, node, path)
        else:
            return self.findPath(root.left, node, path)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = self.findPath(root, p, [])
        q_path = self.findPath(root, q, [])

        result = None

        for i in range(0, min(len(p_path), len(q_path))):
            if p_path[i] != q_path[i]:
                result = p_path[i - 1]
                break

        if not result:
            result = p_path[-1] if len(p_path) < len(q_path) else q_path[-1]
       
        return result