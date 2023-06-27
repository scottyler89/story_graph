
import unittest
from src.narrative_graph import Node, Edge, Graph, Narrative

class TestNarrativeGraph(unittest.TestCase):
    def setUp(self):
        self.node = Node('Test')
        self.graph = Graph()
        self.narrative = Narrative()

    def test_node_creation(self):
        self.assertEqual(self.node.name, 'Test')
        self.assertEqual(self.node.traits, {})
        self.assertEqual(self.node.connections, [])

    def test_graph_creation(self):
        self.assertEqual(self.graph.nodes, {})
        self.assertEqual(self.graph.edges, [])

    def test_narrative_creation(self):
        self.assertEqual(self.narrative.graphs, {})

if __name__ == '__main__':
    unittest.main()

