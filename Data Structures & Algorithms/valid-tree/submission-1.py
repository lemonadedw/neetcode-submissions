from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        if n != len(edges) + 1:
            return False
        
        graph = defaultdict(list)
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        queue = deque([edges[0][0]])
        visited.add(edges[0][0])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == n
        