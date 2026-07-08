class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        nodes = set()
        for i in range(n):
            nodes.add(i)

        components = set()
        for i in range(len(edges)):
            queue = deque([edges[i][0]])
            visited = set()

            while queue:
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                    for nei in graph[node]:
                        queue.append(nei)

            components.add(tuple(visited))
            nodes = nodes.difference(visited)

        return len(components) + len(nodes)