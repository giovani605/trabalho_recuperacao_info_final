import pickle
from operator import itemgetter
import matplotlib.pyplot as plt
import networkx as nx
#por enquanto nao vou te usar
def normalize(G,lista_rage):
    maior = 0
    menor = 1
    for n in listagrafo:
        if maior < resultado[n]:
            maior = resultado[n]
        if menor > resultado[n]:
            menor = resultado[n]


grafo = pickle.load(open('grafo_fucaraocor.pkl'))
grafo2 = pickle.load(open('grafo_postcor.pkl'))
resultado = nx.pagerank(grafo)
listagrafo = nx.to_dict_of_lists(grafo)
for gg in listagrafo:
    teste = resultado[gg] *100
    resultado[gg] =  " " + str(teste)
    print resultado[gg]

g2 = nx.relabel_nodes(grafo,resultado)


#nx.set_node_attributes(grafo,"node_size",resultado)

#print nx.density(grafo)
posi = nx.spring_layout(grafo,iterations=200,scale=200)
nx.draw_random(grafo,dim=20,k=0.2,edge_color='red',font_color='black',width=1,font_size=10,with_labels=True,arrows=True)
#nx.draw_random(grafo2,dim=20,k=0.02,egde_width=0.1,font_color='red',width=0.2,font_size=10,with_labels=True,arrows=True)

#node_and_degree = grafo.degree()
#(largest_hub, degree) = sorted((node_and_degree), key=itemgetter(1))[-1]
# Create ego graph of main hub
#hub_ego = nx.ego_graph(grafo, largest_hub)
# Draw graph
#pos = nx.spring_layout(hub_ego)
#nx.draw(hub_ego, pos, node_color='b', node_size=50, with_labels=True)
# Draw ego as large and red
#nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], node_size=300, node_color='r')

plt.show()
