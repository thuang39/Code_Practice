import csv
import math
import numpy as np
import networkx as nx
from collections import deque
import itertools

arr = np.genfromtxt('amazon0302.txt',dtype='int')
g = nx.DiGraph()
for i in range(0,len(arr)):
    g.add_edge(arr[i,0],arr[i,1])
unionlist = []
maxlist = []
activatedlist = []
counterlist = []
budget = 10
threshold = 2 #1/out_degree >= 0.5 == out_degree <= 2
node = []
for n in range(0,262111):
    if g.out_degree(n) != 0 and g.out_degree(n) <= threshold:
        node.append(n) #filter out all nodes can be activated initially

def maxcascade():
    global activate
    global activated
    global counter
    while activated != activate:
        for n in activate:
            if n not in activated and g.out_degree(n) != 0 and g.out_degree(n) <= threshold:
                for s in g.successors(n):
                    activate.append(s)
            activated.append(n)

for row in node:
    activated = [] #initiate already activated nodes list
    activate = [] #initiate newly activate nodes list
    activate.append(row)
    maxcascade()
    activatedlist.append(activated)
    counterlist.append(len(activated))
activatedlist = sorted(activatedlist, key = lambda x: len(x), reverse=True)
print activatedlist[:10]
length = 0
s = set()
for item in activatedlist[:2]:
    s = s | set(item)
print s
