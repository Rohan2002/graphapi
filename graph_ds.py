from typing import Dict
class Vertex:
    __slots__ = "_element"

    def __init__(self, element) -> None:
        self._element = element
    
    def element(self):
        return self._element
    
    def __hash__(self) -> int:
        return hash(self._element)
    
    def __repr__(self) -> str:
        return f"Vertex(element={self.element()})"

class Edge:
    __slots__ = "_origin", "_destination", "_weight"

    def __init__(self, origin: Vertex, destination: Vertex, weight=None) -> None:
        # Do not instantiate Edge class.
        self._origin = origin
        self._destination = destination
        self._weight = weight
    
    def endpoints(self):
        return (
            self._origin,
            self._destination
        )
    
    def opposite(self, v: Vertex):
        if v is self._origin:
            return self._destination
        else:
            return self._origin
    
    def weight(self):
        return self._weight
    
    def __hash__(self):
        return hash((
            self._origin,
            self._destination
        ))
    def __repr__(self) -> str:
        return f"Edge(origin={self._origin}, destination={self._destination}, weight={self._weight})"

ADJ_MAP_TYPING = Dict[Vertex, Dict[Vertex, Edge]]
class Graph:
    # Adj map implementation
    """
        V is a list of vertices of
        Graph G.
    
        V = [
            V -> {
                Vertex(U): Edge(U, V),
                Vertex(W): Edge(W, V)
            }

            U -> {
                Vertex(V): Edge(V, U),
                Vertex(W): Edge(W, U)
            }

            W -> {
                Vertex(U): Edge(U, W),
                Vertex(V): Edge(V, W),
                Vertex(Z): Edge(Z, W),
            }
            Z -> {
                Vertex(W): Edge(W, Z)
            }
        ]
    """
    def __init__(self, directed=False) -> None:
        self._outgoing: ADJ_MAP_TYPING = {

        }
        self._incoming: ADJ_MAP_TYPING = {

        } if directed else self._outgoing
    
    def is_directed(self):
        # Outgoing vertices != Incoming vertices then 
        # graph is directed.
        return self._outgoing is not self._incoming
    
    def vertex_count(self):
        return len(
            self._outgoing
        )
    
    def vertices(self):
        return self._outgoing.keys()
    
    def edges(self):
        edges_set = set()
        for connected_vertices in self._outgoing.values():
            connected_vertices_edges = connected_vertices.values()
            edges_set.update(connected_vertices_edges)
        return edges_set
    
    def edge_count(self) -> int:
        # Count the number of outgoing edges
        total = sum(len(self._outgoing[vertex]) for vertex in self.vertices())
        return total if self.is_directed() else total // 2
    
    def get_edge(self, u:Vertex, v:Vertex) -> Edge:
        # Return the edge from u to v or None if not
        # adjacent.
        return self._outgoing[u].get(v)

    def degree(self, v: Vertex, outgoing=True):
        # if outgoing is True then we will
        # only count the total number of vertices
        # connected to vertex V.
        if outgoing:
            return len(self._outgoing[v])
        else:
            return len(self._incoming[v])
    
    def incident_edges(self, v, outgoing=True):
        connected_edges_to_v = self._outgoing[v] if outgoing else self._incoming[v]
        return connected_edges_to_v.values()
    
    def insert_vertex(self, vertex: Vertex):
        self._outgoing[vertex] = {}
        if self.is_directed():
            self._incoming[vertex] = {}
        return vertex
    
    def insert_edge(self, edge: Edge):
        origin, destination = edge.endpoints()
        self._outgoing[origin][destination] = edge
        if self.is_directed():
            self._incoming[destination][origin] = edge
        return edge
    
    def __repr__(self) -> str:
        stdout_str = ""
        for vertex in self.vertices():
            if self.degree(vertex) == 0:
                stdout_str += f"{vertex} is not connected to anything.\n"
                continue
            stdout_str += f"{vertex} is connected to\n"
            stdout_str += "\t"
            for idx, connected_vertex in enumerate(self._outgoing[vertex]):
                stdout_str += f"{connected_vertex} with\n" if idx < 1 else f"\n\t{connected_vertex} with\n" 
                stdout_str += f"\t{self.get_edge(vertex, connected_vertex)}\n"
            stdout_str += "\n"
        return stdout_str
