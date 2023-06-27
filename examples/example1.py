
from src.narrative_graph import Node, Edge, Graph, Narrative

# Creating a narrative
narrative = Narrative()

# Adding a graph (Act 1) to the narrative
act1 = narrative.add_graph('Act 1')

# Adding nodes (characters/concepts) to the Act 1 graph
character1 = act1.add_node('Character1', {'trait1': 'value1'})
character2 = act1.add_node('Character2', {'trait2': 'value2'})

# Adding an edge (relationship/interaction) between characters in the Act 1 graph
relationship1 = act1.add_edge('Character1', 'Character2', 'Friendship', '10:00', 'Beginning')

# Printing the nodes and their connections
for node_name, node in act1.nodes.items():
    print(f'Node Name: {node_name}, Connections: {[conn.name for conn in node.connections]}')

# Printing the edges and their attributes
for edge in act1.edges:
    print(f'Start Node: {edge.start_node.name}, End Node: {edge.end_node.name}, Story Arc: {edge.story_arc}')

