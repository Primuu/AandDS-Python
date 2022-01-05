from enum import Enum
from typing import Any, Callable
from typing import Optional
from typing import Dict, List
from Queue import Queue


class EdgeType(Enum):
    # enumerator class containing the edge types
    directed = 1
    undirected = 2


class Vertex:
    # class that stores vertex of the graph
    data: Any
    index: int  # position number in the neighborhood list

    def __init__(self, data: Any, index: int) -> None:
        self.data = data
        self.index = index

    def __repr__(self) -> str:
        return f'{self.index}: {self.data}'


class Edge:
    # class that stores edges of the graph
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self) -> str:
        return f'{self.destination}'


class Graph:
    # class that stores structure of the graph
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self) -> None:
        self.adjacencies = {}

    def __repr__(self) -> str:
        returned_str = ""
        for key_vertex in self.adjacencies:
            returned_str += f'- {key_vertex} ----> {self.adjacencies[key_vertex]}\n'
        return returned_str

    def create_vertex(self, data: Any) -> None:
        self.adjacencies[Vertex(data, len(self.adjacencies))] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge.name == "directed":
            self.add_directed_edge(source, destination, weight)
        if edge.name == "undirected":
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        visited_vertex = []
        queue = Queue()
        list_of_keys = [key for key in self.adjacencies.keys()]
        queue.enqueue(list_of_keys[0])
        while len(queue) > 0:
            v = queue.dequeue()
            visit(v)
            visited_vertex.append(v)
            for neighbour in self.adjacencies[v]:
                if neighbour.destination not in visited_vertex:
                    queue.enqueue(neighbour.destination)

    def dfs(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]) -> None:
        visit(v)
        visited.append(v)
        for neighbour in self.adjacencies[v]:
            if neighbour.destination not in visited:
                self.dfs(neighbour.destination, visited, visit)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        visited_vertex = []
        list_of_keys = [key for key in self.adjacencies.keys()]
        self.dfs(list_of_keys[0], visited_vertex, visit)

    # def show(self):


graph = Graph()
graph.create_vertex("v0")
graph.create_vertex("v1")
graph.create_vertex("v2")
graph.create_vertex("v3")
graph.create_vertex("v4")
graph.create_vertex("v5")
keys = [key for key in graph.adjacencies.keys()]
graph.add_directed_edge(keys[0], keys[1])
graph.add_directed_edge(keys[0], keys[5])
graph.add_directed_edge(keys[5], keys[1])
graph.add_directed_edge(keys[5], keys[2])
graph.add_directed_edge(keys[2], keys[1])
graph.add_directed_edge(keys[2], keys[3])
graph.add_directed_edge(keys[3], keys[4])
graph.add_directed_edge(keys[4], keys[1])
graph.add_directed_edge(keys[4], keys[5])

print(graph)
print("\n")
graph.traverse_breadth_first(print)
print("\n")
graph.traverse_depth_first(print)



# - 0: v0 ----> [1: v1, 5: v5]
# - 1: v1 ----> [0: v0, 5: v5, 2: v2, 4: v4]
# - 2: v2 ----> [1: v1, 5: v5, 3: v3]
# - 3: v3 ----> [4: v4, 2: v2]
# - 4: v4 ----> [1: v1, 3: v3, 5: v5]
# - 5: v5 ----> [0: v0, 1: v1, 2: v2, 4: v4]














