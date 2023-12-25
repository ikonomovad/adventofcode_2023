import networkx as nx

with open('input.txt') as file:
    wiring_diagram = [row.split(': ') for row in file.read().split('\n')]

    # Initialize graph
    G = nx.Graph()

    for line in wiring_diagram:
        c1 = line[0]
        components = line[1].split()

        for co in components:
            G.add_edge(c1, co)

    # https://networkx.org/documentation/latest/reference/algorithms/generated/networkx.algorithms.connectivity.cuts.minimum_edge_cut.html#minimum-edge-cut
    to_cut = nx.minimum_edge_cut(G)

    # Removing edges that can be cut
    G.remove_edges_from(to_cut)

    # Get connected components after removal
    g1, g2 = list(nx.connected_components(G))

    res = len(g1) * len(g2)
    print(res)
