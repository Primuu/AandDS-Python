from enum import Enum
from typing import Any, Callable
from typing import Optional
from typing import Dict, List
from Queue import Queue
from graphviz import Digraph
import math


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

    def show(self, name: Optional = "graph") -> None:
        graph = Digraph()
        visited = []
        for x in self.adjacencies.keys():
            self.show_support(x, graph, visited)
        graph.render(f'output/{name}', directory='E:\\AiSDPythonProjects\\AandDS-Python\\Graph',
                     view=True, format="jpg")

    def show_support(self, vertex: Vertex, graph, visited: List) -> None:
        if vertex not in visited:
            graph.node(str(vertex.index), str(vertex.data))
            visited.append(vertex)
            for neighbour in self.adjacencies[vertex]:
                _weight = ""
                if neighbour.weight is not None:
                    _weight += f"{neighbour.weight}"
                graph.edge(str(neighbour.source.index), str(neighbour.destination.index), label=_weight)
                if not (neighbour.destination in visited):
                    self.show_support(neighbour.destination, graph, visited)


class GraphPath:
    cost_tab = Dict[Vertex, float]
    parents_tab = Dict[Vertex, List[Vertex]]
    visited = List[Vertex]
    path: List[Vertex]

    def __init__(self, graph: Graph, starting_v: Vertex, end_v: Vertex, name: Optional = "graph"):
        self.cost_tab = dict()
        self.parents_tab = dict()
        self.visited = list()
        self.path = list()
        for v in graph.adjacencies.keys():
            self.cost_tab[v] = math.inf
            self.parents_tab[v] = None
        for neighbour in graph.adjacencies[starting_v]:
            self.cost_tab[neighbour.destination] = neighbour.weight
            self.parents_tab[neighbour.destination] = neighbour.source
        self.__search_shortest_way(graph, starting_v, end_v)
        graph_viz = Digraph()
        visited_viz = []
        for x in graph.adjacencies.keys():
            self.__show(x, graph_viz, visited_viz, graph)
        graph_viz.render(f'output/{name}_shortest_path', directory='E:\\AiSDPythonProjects\\AandDS-Python\\Graph',
                         view=True, format="jpg")
        print(f"Path cost: {self.cost_tab[end_v]}")

    def __shortest_path_dijkstra(self, graph: Graph, starting_v: Vertex, end_v: Vertex):
        self.visited.append(starting_v)
        v = min(self.cost_tab, key=self.cost_tab.get)
        while v is not None:
            self.visited.append(v)
            c = self.cost_tab[v]
            for edge in graph.adjacencies[v]:
                nc = c + edge.weight
                if self.cost_tab[edge.destination] > nc:
                    self.cost_tab[edge.destination] = nc
                    self.parents_tab[edge.destination] = edge.source
            cost_copy = self.cost_tab.copy()
            v = min(cost_copy, key=cost_copy.get)
            while min(cost_copy, key=cost_copy.get) in self.visited:
                cost_copy.pop(min(cost_copy, key=cost_copy.get))
                if len(cost_copy.keys()) == 0:
                    v = None
                    break
                v = min(cost_copy, key=cost_copy.get)
        while end_v is not None:
            self.path.append(end_v)
            end_v = self.parents_tab[end_v]
        self.path.reverse()

    def __shortest_path_breadth(self, graph: Graph, starting_v: Vertex, end_v: Vertex) -> None:
        queue = Queue()
        queue.enqueue([starting_v])
        while len(queue) > 0:
            p = queue.dequeue()
            v = p[-1]
            for neighbour in graph.adjacencies[v]:
                if neighbour.destination not in self.visited:
                    np = p.copy()
                    np.append(neighbour.destination)
                    self.visited.append(neighbour.destination)
                    queue.enqueue(np)
                    if neighbour.destination == end_v:
                        self.path = np

    def __search_shortest_way(self, graph: Graph, starting_v: Vertex, end_v: Vertex) -> None:
        edge_list = [y for x in graph.adjacencies.values() for y in x]
        weight = 0
        for w in edge_list:
            if w.weight is not None:
                weight = weight + w.weight
        if weight == 0:
            self.__shortest_path_breadth(graph, starting_v, end_v)
        else:
            self.__shortest_path_dijkstra(graph, starting_v, end_v)

    def __show(self, vertex: Vertex, graph_viz, visited_viz: List, graph: Graph) -> None:
        if vertex not in visited_viz:
            graph_viz.node(str(vertex.index), str(vertex.data))
            visited_viz.append(vertex)
            for neighbour in graph.adjacencies[vertex]:
                _weight = ""
                if neighbour.weight is not None:
                    _weight += f"{neighbour.weight}"
                path_to_color = False
                for x in range(1, len(self.path)):
                    if (self.path[x - 1] == neighbour.source) & (self.path[x] == neighbour.destination):
                        path_to_color = True
                if path_to_color:
                    graph_viz.edge(str(neighbour.source.index), str(neighbour.destination.index),
                                   label=_weight, color="green")
                else:
                    graph_viz.edge(str(neighbour.source.index), str(neighbour.destination.index),
                                   label=_weight)
                if not (neighbour.destination in visited_viz):
                    self.__show(neighbour.destination, graph_viz, visited_viz, graph)


# without weights
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

gp = GraphPath(graph_, keys[3], keys[5])

# weighted graph
graph_w = Graph()
graph_w.create_vertex("A")
graph_w.create_vertex("B")
graph_w.create_vertex("C")
graph_w.create_vertex("D")
keys_w = [key for key in graph_w.adjacencies.keys()]
graph_w.add_directed_edge(keys_w[0], keys_w[1], 30)
graph_w.add_directed_edge(keys_w[0], keys_w[2], 10)
graph_w.add_directed_edge(keys_w[1], keys_w[3], 2)
graph_w.add_directed_edge(keys_w[2], keys_w[3], 9)
graph_w.add_directed_edge(keys_w[2], keys_w[1], 5)

print(graph_w)
print("\n")
graph_w.traverse_breadth_first(print)
print("\n")
graph_w.traverse_depth_first(print)

graph_w.show()

gp_w = GraphPath(graph_w, keys_w[0], keys_w[3])
