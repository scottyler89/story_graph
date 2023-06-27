
class Node:
    """Represents a character or concept in the narrative."""

    def __init__(self, name, traits=None):
        """Initialize a node with a name and optional traits."""
        self.name = name
        self.traits = traits if traits else {}
        self.connections = []

    def update_traits(self, new_traits):
        """Update the traits of the node."""
        self.traits.update(new_traits)


class Edge:
    """Represents an interaction or relationship between nodes."""

    def __init__(self, start_node, end_node, story_arc, timestamp, stage, weight=1):
        """Initialize an edge with start and end nodes, a story arc, timestamp, stage, and weight."""
        self.start_node = start_node
        self.end_node = end_node
        self.story_arc = story_arc
        self.timestamp = timestamp
        self.stage = stage
        self.weight = weight


class Graph:
    """Represents a network of nodes and edges."""

    def __init__(self):
        """Initialize a graph with empty lists of nodes and edges."""
        self.nodes = {}
        self.edges = []

    def add_node(self, name, traits=None):
        """Create and add a node to the graph."""
        node = Node(name, traits)
        self.nodes[name] = node
        return node

    def add_edge(self, start_node_name, end_node_name, story_arc, timestamp, stage, weight=1):
        """Create and add an edge to the graph, update node connections."""
        start_node = self.nodes.get(start_node_name)
        end_node = self.nodes.get(end_node_name)
        if start_node and end_node:
            edge = Edge(start_node, end_node, story_arc, timestamp, stage, weight)
            self.edges.append(edge)
            start_node.connections.append(end_node)
            end_node.connections.append(start_node)
            return edge

    def find_node(self, name):
        """Find a node in the graph by name."""
        return self.nodes.get(name, None)


class Narrative:
    """Represents a narrative composed of multiple graphs (acts)."""

    def __init__(self):
        """Initialize a narrative with an empty dictionary of graphs."""
        self.graphs = {}

    def add_graph(self, name):
        """Create and add a graph to the narrative."""
        graph = Graph()
        self.graphs[name] = graph
        return graph

    def remove_graph(self, name):
        """Remove a graph from the narrative if it exists."""
        if name in self.graphs:
            del self.graphs[name]

    def get_graph(self, name):
        """Get a graph from the narrative by name."""
        return self.graphs.get(name, None)

