import networkx as nx
import matplotlib.pyplot as plt

# You may find it useful to interactively test code using `ipython -pylab`,
# which combines the power of ipython and matplotlib and provides a convenient
# interactive mode.
#
# To test if the import of `networkx.drawing` was successful draw `G` using one of

G = nx.complete_graph(100)
preds = nx.resource_allocation_index(G, [(0, 1), (2, 3),(40,50)])
for u, v, p in preds:
    print('(%d, %d) -> %.8f' % (u, v, p))


    
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
#plt.subplot(122)
#nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

# when drawing to an interactive display.  Note that you may need to issue a
# Matplotlib

plt.show()

