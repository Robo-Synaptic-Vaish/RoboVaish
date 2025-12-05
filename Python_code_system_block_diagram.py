import matplotlib.pyplot as plt
import networkx as nx

def fig1_system_block_diagram():
    G = nx.DiGraph()

    nodes = ["Controller", "Chirp", "Robot", "FSM", "Cipher", "Radio"]
    edges = [("Controller", "Chirp"), ("Chirp", "Robot"), ("Robot", "FSM"),
             ("FSM", "Cipher"), ("Cipher", "Radio")]

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    pos = {
        "Controller": (0, 0),
        "Chirp": (1, 0),
        "Robot": (2, 0),
        "FSM": (3, 0),
        "Cipher": (4, 0),
        "Radio": (5, 0)
    }

    plt.figure(figsize=(10, 2))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=4000, 
            arrowsize=30, font_size=12, font_weight='bold', edge_color='black')
    plt.title("FIG. 1: System Block Diagram", fontsize=16, weight='bold')
    plt.axis('off')
    plt.show()

fig1_system_block_diagram()
