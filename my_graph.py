import networkx as nx
import matplotlib.pyplot as plt
from random import randrange
import random

def random_tuple(degree, G, k):
    return (randrange(degree), randrange(degree))


def connect_alone(G, k, E):
    '''Conectar los vertices que estan aislados a los nodos que no han excedido su tope '''
    # Añadir en una cola los aislados
    isolatednodes_list = list()
    for node in G.nodes:
        if len(list(G.neighbors(node))) == 0:
            isolatednodes_list.append(node)

    if(len(isolatednodes_list) > 0):
        for node in G.nodes:
            if len(isolatednodes_list) != 0 and len(list(G.neighbors(node))) != 0 and len(list(G.neighbors(node))) < k and len(G.edges) < E:
                poped = isolatednodes_list.pop()
                G.add_edge(node, poped)

def graph_img(v, k, E):
    plt.clf()
    G = nx.complete_graph(v)
    # ELIMINAR ARISTAS EXTRA GENERADAS POR EL GRAFO COMPLETO
    # Esto borra aquellas conexiones que excedan el parametro K
    for node in G.nodes:
        if len(list(G.neighbors(node))) > k:
            dif = len(list(G.neighbors(node))) - k
            for i in range(0, dif):
                G.remove_edge(node, random.choice(list(G.neighbors(node))))

    while len(G.edges) > E:
        tup = random_tuple(v, G, k)
        if tup in G.edges:
            G.remove_edge(tup[0], tup[1])
    connect_alone(G, k, E)

    vecinos = {}
    for node in G.nodes:
        vecinos[node] = list(G.neighbors(node))

    node_color = [G.degree(v) for v in G]
    colorss = [plt.cm.Reds, plt.cm.Blues, plt.cm.Greens]
    nx.draw_networkx(G, pos=nx.spring_layout(G, k=0.55), node_size=400, node_color=node_color, alpha=.9, with_labels=True,
                     edge_color='.5', cmap=random.choice(colorss))
    print("Edges: ", len(G.edges))
    print("Nodes: ", G.nodes)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("graph.png", dpi=620)
    plt.clf()
    plt.close()
    return vecinos
