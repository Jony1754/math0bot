import networkx as nx
import matplotlib.pyplot as plt
from random import randrange
import random


def connect_alone(G, k):
    '''Conectar los vertices que estan aislados a los nodos que no han excedido su tope '''
    # Añadir en una cola los aislados
    isolatednodes_list = list()
    for node in G.nodes:
        if len(list(G.neighbors(node))) == 0:
            isolatednodes_list.append(node)

    # print("ISOLATED NODES LIST: ", isolatednodes_list)

    if(len(isolatednodes_list) > 0):
        for node in G.nodes:
            # print(
            #     f"condiciones cumplidas 1: {len(isolatednodes_list) != 0} 2: {len(list(G.neighbors(node))) != 0} 3: {len(list(G.neighbors(node))) < k}", f"CHECKEANDO PAREJA ({node}, {isolatednodes_list[-1 or 0]})")
            if len(isolatednodes_list) != 0 and len(list(G.neighbors(node))) != 0 and len(list(G.neighbors(node))) < k:
                poped = isolatednodes_list.pop()
                # print(f"Se conecto a ({node}, {poped}) :")
                G.add_edge(node, poped)


G = nx.complete_graph(20)
k = 3
for node in G.nodes:
    if len(list(G.neighbors(node))) > k:
        dif = len(list(G.neighbors(node))) - k
        for i in range(0, dif):
            G.remove_edge(node, random.choice(list(G.neighbors(node))))
connect_alone(G, k)
vecinos = {}
for node in G.nodes:
    vecinos[node] = list(G.neighbors(node))
print(vecinos)
cadena = ""
for key in vecinos:
    cadena += f'Vecinos del nodo {key}: {vecinos[key]}\n'

print(cadena)
node_color = [G.degree(v) for v in G]
nx.draw_networkx(G, node_size=400, node_color=node_color, alpha=.9, with_labels=True,
                 edge_color='.5', cmap=plt.cm.Reds)
plt.axis('off')
plt.tight_layout()
plt.savefig("graph.png", dpi=620)
plt.clf()
