import networkx as ntx
import pylab as plt
D=ntx.DiGraph()
D.add_weighted_edges_from([('A','B',1),('A','C',1),('C','A',3),('B','A',3),('B','C',4)])
print(ntx.pagerank(D))
ntx.draw(D,with_labels=True)
plt.show()