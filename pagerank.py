from time import time
import networkx as nx


begin = time()
e = []
with open('D:\WorkSpace\Python\web-Google.txt') as f:
    for line in f:
        o = tuple(line.split())
        e.append(o)

A = nx.DiGraph()
A.add_edges_from(e)
p = nx.pagerank_scipy(A)

end = time()

count = 0
for key in p:
    if count < 10:
        print('p[{0}] = {1}'.format(key, p[key]))
        count += 1
    else:
        break

print("time = {0}".format(end - begin))
