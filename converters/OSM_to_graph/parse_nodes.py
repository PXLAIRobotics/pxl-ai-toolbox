from bs4 import BeautifulSoup
from operator import attrgetter

'''
    TODO    argument support --input --output
'''

nodes = []
edges = []

full = ""
with open('nodes', 'r') as nodefile:
    data=nodefile.read()
    pn = BeautifulSoup(data, "xml")
    # parse nodes
    for node in pn.find_all("node"):
        nodes.append([node['id'], node['lat'], node['lon']])
    # parse edges
    for way in pn.find_all("way"):
        prev = None
        for node in way.find_all("nd"):
            if not prev == None:
                edges.append([prev, node['ref']])
            prev = node['ref']

output = open('output', 'w')
output.write("# NODES\n")
output.write("# NODE;id;lat;lon\n")
for node in nodes: 
    output.write("NODE;%s;%s;%s\n" % (node[0], node[1], node[2]))

output.write("\n# EDGES\n")
output.write("# EDGE;id1;id2\n")
for edge in edges:
    output.write("EDGE;%s;%s\n" % (edge[0], edge[1]))