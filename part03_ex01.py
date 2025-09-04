# part03_ex01.py
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


my_graph = Graph()

# 정점 및 간선 추가
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("B", "D")
my_graph.add_edge("C", "D")
my_graph.add_edge("C", "E")

my_graph.print_graph()
# 출력:
# 정점 A: ['B', 'C']
# 정점 B: ['A', 'D']
# 정점 C: ['A', 'D', 'E']
# 정점 D: ['B', 'C']
# 정점 E: ['C']