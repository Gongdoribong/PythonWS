import networkx as nx
import matplotlib.pyplot as plt

def makeGraph(V,E,Gtype):
    if Gtype == 0 :
        G = nx.Graph()
        print("#무향그래프: ")
    elif Gtype == 1 :
        G = nx.DiGraph()
        print("유향그래프 : ")

    G.add_nodes_from(V)
    G.add_edges_from(E)

    nx.draw(G, with_labels = True,
            node_color = "tab:red", node_size = 800,
            edge_color = "tab:blue", width = 4,
            font_size = 22, alpha = 0.8)
    plt.show()

V = {1,2,3,4}
E = {(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)}

makeGraph(V, E, 0)
makeGraph(V, E, 1)
