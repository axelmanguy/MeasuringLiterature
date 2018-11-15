# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 08:54:47 2018

@author: M Manguy
"""
from io import StringIO
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import sample
import re
file = open("RIGOLETTO.txt", "r")
lines=file.readlines()
character=['DUCA','RIGOLETTO','GILDA','SPARAFUCILE','MADDALENA',
            'GIOVANNA','MONTERONE','MARULLO','BORSA','CONTESSA',
            'PAGGIO','CORO','CEPRANO']
EdgesValues=np.zeros((len(character),len(character)))
for i,data in enumerate(lines):
    line=data.split('[')
    sources=line[0].strip('\n').split(',')
    if len(line)>1:
        line[1]=re.sub("[\n']", '', line[1])
        destinations=line[1].strip().split(']')
        destinations=destinations[0].split(',')
    if line[0].strip('\n') in character and len(line)>1:
        for source in sources:
            print("------")
            print(source)
            for dest in destinations:
                dest=re.sub("[ ]", '', dest)
                if re.search(' /', dest) is not None:
                    pass
                else:
                    print(dest)
                    EdgesValues[character.index(source),character.index(dest)]+=1
print(EdgesValues)
A=np.matrix(EdgesValues)
G=nx.from_numpy_matrix(A,create_using = nx.MultiDiGraph())
#label design
labels={}
for i,char in enumerate(character):
    labels[i]=char
nx.draw(G,pos=nx.nx_agraph.graphviz_layout(G),
		labels=labels,with_labels=True,arrows=True,
		node_color='coral',font_size=12,arrowstyle='fancy',
		edge_color='cadetblue',font_color='crimson',font_weight='bold')
plt.show()