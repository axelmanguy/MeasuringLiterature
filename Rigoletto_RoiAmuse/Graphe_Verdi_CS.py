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
import pprint as pp
import matplotlib as mpl
import copy
file = open("Giuseppe Verdi - Rigoletto (Italian–English)_modified.txt", "r",encoding='utf8')
lines=file.readlines()
character=['DUCA',
           'RIGOLETTO',
           'GILDA',
           'SPARAFUCILE',
           'MADDALENA',
           'GIOVANNA',
           'MONTERONE',
           'MARULLO',
           'BORSA',
           'CONTESSA',
           'PAGGIO',
           'CORO',
           'CEPRANO']
EdgesValues=np.zeros((len(character),len(character)))
for i,data in enumerate(lines):
    line=data.split('[')
    j=0
    number=0
    if data.strip('\n') == 'FINE':
        break
    while lines[i+j] !='\n':
        j+=1
        number += len(lines[i+j].split(' '))
    #print(number)    
    sources=line[0].strip('\n').split(',')
    if len(line)>1:
        line[1]=re.sub("[\n']", '', line[1])
        destinations=line[1].strip().split(']')
        destinations=destinations[0].split(',')
    if line[0].strip('\n') in character and len(line)>1:
        for source in sources:
            #print("------")
            #print(source)
            for dest in destinations:
                dest=re.sub("[ ]", '', dest)
                if re.search(' /', dest) is not None:
                    pass
                else:
                    #print(dest)
                    EdgesValues[character.index(source),character.index(dest)]+=number
names,values=[],[]
for i,char in enumerate(character):
    names.append(char)
    print(100*(np.sum(EdgesValues[i])/(np.sum(np.sum(EdgesValues)))))
    values.append(100*(np.sum(EdgesValues[i])/(np.sum(np.sum(EdgesValues)))))
values=np.array(values)
names2=[character[i] for i in values.argsort()]
print(names2)
values2=np.sort(values)
print(values2)
plt.bar(names2, values2)
plt.xticks(rotation=45)
plt.yticks(rotation=90)
plt.title("Le Roi s'amuse character space")
plt.show()

pp.pprint(EdgesValues)
print('----------------------')
print(np.min(EdgesValues))
print(np.max(EdgesValues))
print('----------------------')
A=np.matrix(EdgesValues)
B=copy.deepcopy(A)
B=np.delete(B, 1, 0)
B=np.delete(B, 1, 1)
B=np.delete(B, 0, 0)
B=np.delete(B, 0, 1)
G=nx.from_numpy_matrix(B,create_using = nx.MultiDiGraph())
#Edge calculation
print(B)
print(A)
colors=[B[x,y] for x,y in G.edges()]
#label design
labels={}
character=['GILDA',
           'SPARAFUCILE',
           'MADDALENA',
           'GIOVANNA',
           'MONTERONE',
           'MARULLO',
           'BORSA',
           'CONTESSA',
           'PAGGIO',
           'CORO',
           'CEPRANO']
for i,char in enumerate(character):
    labels[i]=char
print(labels)
fig = plt.figure()
nx.draw(G,pos=nx.nx_agraph.graphviz_layout(G),
		labels=labels,with_labels=True,arrows=False,
       edge_color=colors,edge_cmap=plt.cm.YlOrRd,width=2,
		node_color='cadetblue',font_size=12,
       font_color='darkolivegreen',font_weight='bold')
fig.patch.set_facecolor("#353432")
mpl.rcParams['savefig.facecolor'] = "#353432"
plt.savefig('CS_Rigoletto_Gilda.png')
plt.show()
