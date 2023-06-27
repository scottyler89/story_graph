
import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(graph, graph_name):
    G = nx.Graph()
    # add nodes
    for node_name, node in graph.nodes.items():
        G.add_node(node_name, traits=node.traits)
    # add edges
    for edge in graph.edges:
        G.add_edge(edge.start_node.name, edge.end_node.name, weight=edge.weight, story_arc=edge.story_arc, stage=edge.stage)
    # draw the graph
    pos = nx.spring_layout(G)  # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)
    # edges
    nx.draw_networkx_edges(G, pos, width=6)
    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    plt.title(graph_name)
    plt.axis('off')
    plt.show()


def visualize_narrative(narrative):
    for graph_name, graph in narrative.graphs.items():
        visualize_graph(graph, graph_name)

