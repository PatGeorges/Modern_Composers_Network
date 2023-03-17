import csv
from operator import itemgetter
import numpy as np
import networkx as nx
#import community
from networkx.algorithms import community
#import pylab as plt
import matplotlib.pyplot as plt
from fa2 import ForceAtlas2
import random

#For Figures 5, 7,8
random.seed(148)
np.random.seed(2007)

A = np.genfromtxt("Adjacency_matrix_modern_composers.csv", delimiter=',')
G=nx.DiGraph(A) # for directed graph
print(nx.info(G))

forceatlas2 = ForceAtlas2(
# Behavior alternatives
outboundAttractionDistribution=False, # True = Dissuade hubs
linLogMode=False, # Not implemented
adjustSizes=False, # Prevent overlap   Not implemented
edgeWeightInfluence=1.0,
# Performance
jitterTolerance=1.0,
barnesHutOptimize=True,
barnesHutTheta=1.2,
multiThreaded=False,
# Tuning
# Intial values/setting.  sR= 2.0, gravity = 0.
#sR = 0.001 and 0.01 and gravity = 3.0  OK results
scalingRatio=1.0,
#gravity=5.0,
gravity = 1,
#scalingRatio=2.0,
#gravity=0.0,
strongGravityMode=False,
# Log
verbose=True)

pos= forceatlas2.forceatlas2_networkx_layout(G, iterations=2000)

# making labels
import csv
def make_label_dict(labels):
    l={}
    for i, label in enumerate(labels, start=0):
        l[i] = label
    return l
with open('Labels_column_modern_composers.csv', 'r', encoding = "ISO-8859-1") as f:
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames
labels=make_label_dict(headers)
print(labels)

with open('Nodelist_modern_composers.csv','r', encoding = "ISO-8859-1") as nodecsv:
  nodereader = csv.reader(nodecsv)
  nodes = [n for n in nodereader][1:]
node_list = [n[0] for n in nodes]  # get a list of only the node ranks

#print(node_list)
#print(len(node_list))

birth_dict = {}
mid_life_dict = {}
death_dict = {}
period_dict = {}
rank_dict = {}
nationality_dict = {}
name_dict = {}
period_dict ={}
period_agg_dict ={}
period_agg_colour_dict = {}
nationality_agg_colour_dict = {}
Unique_Style_colour_dict = {}
Sex_Race_dict = {}
for node in nodes:
    birth_dict[node[1]]=node[2]
    mid_life_dict[node[1]]=node[3]
    death_dict[node[1]]=node[4]
    rank_dict[node[1]] = node[0]
    nationality_dict[node[1]]=node[5]
    period_dict[node[1]]=node[7]
    name_dict[node[1]]=node[1]
    period_dict[node[1]]=node[16]
    period_agg_dict[node[1]]=node[17]
    period_agg_colour_dict[node[1]]=node[18]
    nationality_agg_colour_dict[node[1]]=node[22]
    Unique_Style_colour_dict[node[1]]=node[24]
    Sex_Race_dict[node[1]]=node[25]
#print(birth_dict)
#print(rank_dict)
#print(period_dict)

d = dict(G.degree)
d_out = dict(G.out_degree)
d_in = dict(G.in_degree)

node_size = [(v+2)*10 for v in d_out.values()] # node size in function of how much the composer influenced others

#node_color = [x for x in period_agg_colour_dict.values()]
#node_color = [x for x in Unique_Style_colour_dict.values()]  # Figure 5 Scientometrics paper
node_color = [x for x in nationality_agg_colour_dict.values()]  #Figure 7 Scientometrics paper
#node_color = [x for x in Sex_Race_dict.values()]  #Figure 8 Scientometrics paper

fig, ax = plt.subplots(figsize=(60, 40))

nodes=nx.draw_networkx_nodes(G, pos=pos, node_size = node_size, node_color=node_color, alpha=0.6)
labels=nx.draw_networkx_labels(G, pos=pos, labels=labels, font_size = 5, font_color='k', alpha=1)
#edge_color = 'grey'
edge_color = 'y'
edges=nx.draw_networkx_edges(G, pos=pos, width= 0.2, edge_color=edge_color, style ='dotted',alpha=0.2)
#plt.title("Modern composers'network of influences\n ForceAtlas2_layout\n Author: Patrick Georges -- pgeorges@uottawa.ca")

#plt.savefig('Modern_composer_network_by_style.png')  # Figure 5 Scientometrics paper
plt.savefig('Modern_composer_network_by_citizenship.png')  #Figure 7 Scientometrics paper
#plt.savefig('Modern_composer_network_by_gender&ethnicity.png')   #Figure 8 Scientometrics paper
plt.show()
