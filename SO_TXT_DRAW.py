import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

## SET RANDOM SEED
# import random
# from numpy import random as nprand
# seed = hash("random") % 2 ** 32
# nprand.seed(seed)
# random.seed(seed)
#####################################
# configurate default figure size
plt.rcParams.update({"figure.figsize": (10, 10)})

url_txt = Path("./data/sotest.txt")
G = nx.Graph()

with open(url_txt, "r") as file_obj:
    for i, row in enumerate(file_obj):
        row = row.strip().split()
        if len(row) not in (0, 1):
            self_node = row[0]
            for neighbors in row[1:]:
                G.add_edge(self_node, neighbors)
        elif len(row) == 1:
            if row[0] not in G:
                nx.add_node(row[0])
        else:
            print(f"row {i+1} is empty")

nx.draw_networkx(G)
plt.gca().margins(0.15, 0.15)
plt.show()

nx.write_adjlist(G, "out.adjlist")
