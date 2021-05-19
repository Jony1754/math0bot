import networkx as nx
import matplotlib.pyplot as plt
from random import randrange
import random


def random_tuple(degree):

    return (randrange(degree), randrange(degree))


v = int(input("Ingresa el numero de vertices: "))
E = int(input("Ingresa el numero de aristas: "))
k = int(input("Ingresa el numero maximo de aristas por vertice: "))

# G = nx.Graph()
G = nx.complete_graph(v)
# G.add_edge(1, 2)
# G.add_edge(2, 3)
# G.add_edge(3, 4)
print("Edges: ", G.edges)
print("Nodes: ", G.nodes)

# for i in range(1, v + 1, 1):
#     G.add_node(i)

# for i in range(1, E + 1, 1):
#     for j in range(1, len(G.nodes)):
#         G.add_edge(j,)

print(len(G.edges))
while len(G.edges) > E:
    tup = random_tuple(v)
    if tup in G.edges:
        # print(tup, " existe en la lista")
        G.remove_edge(tup[0], tup[1])
        # print("Se elimino ", tup, "de la lista")
        # print("Edges updated: ", G.edges)

print(len(G.edges))
print("valor de k dado: ", k)
for node in G.nodes:
    print(f"Vecinos del nodo {node}: ", list(G.neighbors(node)))
    if len(list(G.neighbors(node))) > k:
        dif = len(list(G.neighbors(node))) - k
        for i in range(0, dif):
            G.remove_edge(node, random.choice(list(G.neighbors(node))))

print("LISTA DE VECINOS LUEGO DE ELIMINAR")
for node in G.nodes:
    print(f"Vecinos del nodo {node}: ", list(G.neighbors(node)))

nx.draw_networkx(G, with_labels=True)
plt.savefig("filenam2e.png")
plt.clf()
