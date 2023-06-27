
from src import Node, Edge, Graph, Narrative

# Create a new narrative for the movie
up_narrative = Narrative()

# Create a new graph for the first 15 minutes
act_1 = up_narrative.add_graph('First 15 Minutes')

# Add nodes for the main characters
carl = act_1.add_node('Carl', {'age': 'child', 'dream': 'adventurer'})
ellie = act_1.add_node('Ellie', {'age': 'child', 'dream': 'adventurer'})

# Add edges for key events
meet = act_1.add_edge('Carl', 'Ellie', 'Meet at the Club', 'Childhood', 'Introductions')
dream = act_1.add_edge('Carl', 'Ellie', 'Share Adventure Dreams', 'Childhood', 'Dream Sharing')
marriage = act_1.add_edge('Carl', 'Ellie', 'Get Married', 'Young Adulthood', 'Commitment')

# Create node for their shared dream
paradise_falls = act_1.add_node('Paradise Falls', {'type': 'place', 'significance': 'dream destination'})

# Add edge for shared dream
shared_dream = act_1.add_edge('Carl', 'Paradise Falls', 'Dream of Adventure', 'Throughout Life', 'Dreaming')

