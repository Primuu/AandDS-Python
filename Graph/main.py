from enum import Enum
from typing import Any, Callable
from typing import Optional
from typing import Dict, List
from Queue import Queue
from graphviz import Digraph


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

    def show(self):
        filename = "graph"
        graph = Digraph()
        visited = []
        graph_vertices = self.adjacencies.keys()
        for x in graph_vertices:
            self.show_support(x, graph, visited)
        graph.render(filename=filename, directory='E:\\AiSDPythonProjects\\AandDS-Python\\Graph',
                     view=True, format="jpg")

    def show_support(self, vertex: Vertex, graph, visited: List):
        if vertex not in visited:
            graph.node(str(vertex.index), str(vertex.data))
            visited.append(vertex)
            for x in self.adjacencies[vertex]:  # x is a vertex neighbour
                desc = ""
                if x.weight is not None:
                    desc += f"{x.weight}"
                graph.edge(str(x.source.index), str(x.destination.index), label=desc)  # label as a weight
                if not (x.destination in visited):
                    self.show_support(x.destination, graph, visited)


graph_ = Graph()
graph_.create_vertex("v0")
graph_.create_vertex("v1")
graph_.create_vertex("v2")
graph_.create_vertex("v3")
graph_.create_vertex("v4")
graph_.create_vertex("v5")
keys = [key for key in graph_.adjacencies.keys()]
graph_.add_directed_edge(keys[0], keys[1])
graph_.add_directed_edge(keys[0], keys[5])
graph_.add_directed_edge(keys[5], keys[1])
graph_.add_directed_edge(keys[5], keys[2])
graph_.add_directed_edge(keys[2], keys[1])
graph_.add_directed_edge(keys[2], keys[3])
graph_.add_directed_edge(keys[3], keys[4])
graph_.add_directed_edge(keys[4], keys[1])
graph_.add_directed_edge(keys[4], keys[5])

print(graph_)
print("\n")
graph_.traverse_breadth_first(print)
print("\n")
graph_.traverse_depth_first(print)

graph_.show()
