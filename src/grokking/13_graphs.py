from collections import defaultdict


class UnionFind:
    def __init__(self, size: int):
        self.size = size
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u: int):
        if self.parent[u] == u:
            return u
        return self.find(self.parent[u])

    def union(self, u: int, v: int):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.rank[u] < self.rank[v]:
            u, v = v, u
        self.parent[v] = u
        if self.rank[u] == self.rank[v]:
            self.rank[u] += 1


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], start: int, end: int
    ) -> bool:
        graph: dict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    if neighbor == end:
                        return True
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

    def findProvinces(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)

        visited = set()
        counter = 0
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            stack = [i]
            while stack:
                vertex = stack.pop()
                for j in range(n):
                    if (j not in visited) and isConnected[vertex][j]:
                        stack.append(j)
                        visited.add(j)
            counter += 1
        return counter

    def findProvinces(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        counter = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and (uf.find(i) != uf.find(j)):
                    uf.union(i, j)
                    counter -= 1
        return counter

    def eventualSafeNodes(self, graph: list[list[int]]):
        def dfs(node: int):
            if visited[node] == -1:
                return True
            if visited[node] == 1:
                return False
            visited[node] = 1
            for next in graph[node]:
                if not dfs(next):
                    return False
            visited[node] = -1
            return True

        n = len(graph)
        visited = [0] * n
        return [i for i in range(n) if dfs(i)]

    def eventualSafeNodes(self, graph: list[list[int]]):
        from collections import deque

        safe_nodes: list[int] = []
        in_nodes = [[] for _ in range(len(graph))]
        for i, nodes in enumerate(graph):
            for node in nodes:
                in_nodes[node].append(i)

        degrees = [len(item) for item in graph]
        queue = deque([i for i, degree in enumerate(degrees) if degree == 0])

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for in_node in in_nodes[node]:
                degrees[in_node] -= 1
                if degrees[in_node] == 0:
                    queue.append(in_node)
        return sorted(safe_nodes)

    def findSmallestSetOfVertices(
        self, n: int, edges: list[list[int]]
    ) -> list[int]:
        counter = [0] * n
        for _, out_node in edges:
            counter[out_node] += 1
        return [i for i, count in enumerate(counter) if count == 0]

    def findSmallestSetOfVertices(
        self, n: int, edges: list[list[int]]
    ) -> list[int]:
        return [i for i in range(n) if i not in set([out for _, out in edges])]

    def numBusesToDestination(
        self, routes: list[list[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        stop_to_buses = defaultdict(list)
        for bus, route in enumerate(routes):
            for bus_stop in route:
                stop_to_buses[bus_stop].append(bus)

        bus_stop_set = set([source])
        counter = 0
        visited = set()
        while bus_stop_set:
            new_set = set()
            for bus_stop in bus_stop_set:
                if bus_stop == target:
                    return counter
                new_bus_stop = set(
                    [
                        bus_stop
                        for bus in stop_to_buses[bus_stop]
                        for bus_stop in routes[bus]
                        if bus_stop not in visited
                    ]
                )
                new_set = new_set.union(new_bus_stop)
            visited = visited.union(new_set)
            bus_stop_set = new_set
            counter += 1

        return -1
