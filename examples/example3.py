
from narrative_graph import Node, Edge, Graph, Narrative

# Creating a narrative
narrative = Narrative()

# Act 1: Childhood
graph1 = narrative.add_graph('Act 1: Childhood')

# Adding nodes (characters/concepts)
young_Carl = graph1.add_node('Young Carl', {'trait': 'dreamer'})
young_Ellie = graph1.add_node('Young Ellie', {'trait': 'adventurous'})
adventure = graph1.add_node('Adventure', {'trait': 'desire'})

# Adding edges (interactions/relationships)
graph1.add_edge('Young Carl', 'Young Ellie', 'meets', 'minute 1', 'introduction')
graph1.add_edge('Young Ellie', 'Young Carl', 'shares adventure book', 'minute 2', 'developing')
graph1.add_edge('Young Carl', 'Adventure', 'desires', 'minute 2', 'developing')
graph1.add_edge('Young Ellie', 'Adventure', 'desires', 'minute 2', 'developing')

# Act 2: Marriage
graph2 = narrative.add_graph('Act 2: Marriage')

# Updating nodes to represent time passage
adult_Carl = graph2.add_node('Adult Carl', {'trait': 'loving husband'})
adult_Ellie = graph2.add_node('Adult Ellie', {'trait': 'loving wife'})

# Adding edges (interactions/relationships)
graph2.add_edge('Adult Carl', 'Adult Ellie', 'marries', 'minute 4', 'introduction')
graph2.add_edge('Adult Carl', 'Adult Ellie', 'lives happily', 'minute 5-9', 'developing')
graph2.add_edge('Adult Carl', 'Adult Ellie', 'loses', 'minute 10', 'conclusion')

# Act 3: Loneliness
graph3 = narrative.add_graph('Act 3: Loneliness')

# Updating nodes to represent time passage
old_Carl = graph3.add_node('Old Carl', {'trait': 'grieving'})

# Adding edges (interactions/relationships)
graph3.add_edge('Old Carl', 'Adult Ellie', 'misses', 'minute 11-15', 'introduction')
graph3.add_edge('Old Carl', 'Adventure', 'remembers', 'minute 11-15', 'introduction')

# Visualizing the narrative
from narrative_graph.visualization import visualize_narrative
visualize_narrative(narrative)

