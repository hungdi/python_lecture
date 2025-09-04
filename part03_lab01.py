class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        """그래프에 정점을 추가합니다."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v, directed=False):
        """정점 u와 v 사이에 간선을 추가합니다."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u) # 무방향 그래프인 경우

    def print_graph(self):
        """그래프의 내용을 출력합니다."""
        for vertex, neighbors in self.graph.items():
            print(f"정점 {vertex}: {neighbors}")
from collections import deque

# 그래프 구성
g = Graph()
for u, v in [("A","B"), ("A","C"), ("B","D"), ("C","E"), ("D","F"), ("E","G")]:
    g.add_edge(u, v)

def invite_list(g, start, max_hops=2):
    dist = {start: 0}
    q = deque([start])
    out = set()
    while q:
        u = q.popleft()
        for v in g.graph.get(u, []):
            if v not in dist and dist[u] + 1 <= max_hops:
                dist[v] = dist[u] + 1
                out.add(v)
                q.append(v)
    return sorted(out)

print(invite_list(g, "A", 2))