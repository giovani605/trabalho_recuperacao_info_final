import networkx as nx
import networkx.drawing as desenho
import matplotlib.pyplot as plt


G = nx.DiGraph()
G.add_edge("pagina 1","pagina 2")
G.add_edge("pagina 1","pagina 3")


nx.draw_random(G ,with_labels=True, font_weight='bold')
plt.show()


