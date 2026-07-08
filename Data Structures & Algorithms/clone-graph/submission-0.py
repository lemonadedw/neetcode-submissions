"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        ref = {}
        ref[node] = Node(node.val)
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in ref:
                    ref[nei] = Node(nei.val)
                    queue.append(nei)
                ref[cur].neighbors.append(ref[nei])
        
        return ref[node]        