import matplotlib.pyplot as plt
import networkx

def getkmer(seq, k):
    reads = []
    for j in range(0, len(seq) - k + 1):
        reads.append(seq[j:j+k])
    return reads

def debruijn(st, k):
    edges = []
    nodes = set()
    for s in st:
        kmers = getkmer(s, k)
        for i in range(len(kmers) - 1):
            edges.append((kmers[i], kmers[i+1]))
            nodes.add(kmers[i])
            nodes.add(kmers[i+1])
    return edges, nodes

reads = ["TTACGTT","CCGTTA","GTTAC","GTTCGA","CGTTC"]
edges, nodes = debruijn(reads, 5)

def visualize(edges, nodes):
    dbgraph = networkx.DiGraph()
    dbgraph.add_nodes_from(nodes)
    dbgraph.add_edges_from(edges)

    networkx.draw(dbgraph, with_labels=True, node_size=1000)
    plt.show()

visualize(edges, nodes)
