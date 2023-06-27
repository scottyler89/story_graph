import unittest
from src.narrative_graph import Node, Edge, Graph, Narrative

class TestNarrativeGraph(unittest.TestCase):
    def setUp(self):
        self.node = Node('Test')
        self.edge = Edge('Start', 'End', 'Arc', 'Timestamp', 'Stage')
        self.graph = Graph()
        self.narrative = Narrative()

    def test_node_creation(self):
        self.assertEqual(self.node.name, 'Test')
        self.assertEqual(self.node.traits, {})
        self.assertEqual(self.node.connections, [])

    def test_node_update_traits(self):
        self.node.update_traits({'trait1': 'value1'})
        self.assertEqual(self.node.traits, {'trait1': 'value1'})

    def test_edge_creation(self):
        self.assertEqual(self.edge.start_node, 'Start')
        self.assertEqual(self.edge.end_node, 'End')
        self.assertEqual(self.edge.story_arc, 'Arc')
        self.assertEqual(self.edge.timestamp, 'Timestamp')
        self.assertEqual(self.edge.stage, 'Stage')

    def test_graph_creation(self):
        self.assertEqual(self.graph.nodes, {})
        self.assertEqual(self.graph.edges, [])

    def test_graph_add_node(self):
        self.graph.add_node('NewNode', {'trait1': 'value1'})
        self.assertIn('NewNode', self.graph.nodes)

    def test_graph_add_edge(self):
        self.graph.add_node('Node1')
        self.graph.add_node('Node2')
        self.graph.add_edge('Node1', 'Node2', 'Arc', 'Timestamp', 'Stage')
        self.assertEqual(len(self.graph.edges), 1)

    def test_graph_find_node(self):
        self.graph.add_node('FindMe')
        self.assertIsNotNone(self.graph.find_node('FindMe'))

    def test_narrative_creation(self):
        self.assertEqual(self.narrative.graphs, {})

    def test_narrative_add_graph(self):
        self.narrative.add_graph('Graph1')
        self.assertIn('Graph1', self.narrative.graphs)

    def test_narrative_remove_graph(self):
        self.narrative.add_graph('Graph1')
        self.narrative.remove_graph('Graph1')
        self.assertNotIn('Graph1', self.narrative.graphs)

    def test_narrative_get_graph(self):
        self.narrative.add_graph('Graph1')
        self.assertIsNotNone(self.narrative.get_graph('Graph1'))

if __name__ == '__main__':
    unittest.main()

