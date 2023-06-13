import unittest
from graph_ds import Vertex, Edge, Graph
class TestVertex(unittest.TestCase):
    def setUp(self) -> None:
        self.v = Vertex(5)

    def test_vertex(self):
        self.assertEqual(
            self.v._element,
            5
        )

class TestEdge(unittest.TestCase):
    def setUp(self) -> None:
        self._origin = Vertex("A")
        self._dest = Vertex("B")
        self._weight = 0.5

        self._edge = Edge(self._origin, self._dest, weight=self._weight)
        return super().setUp()
    
    def test_edge_endpoints(self):
        o, d = self._edge.endpoints()

        self.assertTrue(o is self._origin)
        self.assertTrue(d is self._dest)
    
    def test_edge_opposite(self):
        origin_opposite = self._edge.opposite(self._origin)
        dest_opposite = self._edge.opposite(self._dest)

        self.assertTrue(
            origin_opposite is self._dest
        )
        self.assertTrue(
            dest_opposite is self._origin
        )
    
    def test_get_weight(self):
        self.assertEqual(
            self._edge.weight(),
            self._weight
        )

class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        # Graph diagram is in graph_example.png
        self.vertices = {
            "V": Vertex(element="V"),
            "U": Vertex(element="U"),
            "W": Vertex(element="W"),
            "Z": Vertex(element="Z"), 
        }
        self.edges = [
            Edge(
                origin=self.vertices["V"], 
                destination=self.vertices["U"],
                weight="e"
            ),
            Edge(
                origin=self.vertices["U"], 
                destination=self.vertices["W"],
                weight="g"
            ),
            Edge(
                origin=self.vertices["V"], 
                destination=self.vertices["W"],
                weight="f"
            ),
            Edge(
                origin=self.vertices["W"], 
                destination=self.vertices["Z"],
                weight="h"
            ),
        ]

        self.undirected_graph = Graph(directed=False)
        self.directed_graph = Graph(directed=True)
        
        for fixture_vertex in self.vertices.values():
            self.undirected_graph.insert_vertex(
                fixture_vertex
            )
            self.directed_graph.insert_vertex(
                fixture_vertex
            )

        for fixture_edge in self.edges:
            self.undirected_graph.insert_edge(
                edge=fixture_edge
            )
            self.directed_graph.insert_edge(
                edge=fixture_edge
            )
        return super().setUp()
    
    def test_graph(self):
        print("\n")
        print(self.undirected_graph)
    
if __name__ == "__main__":
    unittest.main()