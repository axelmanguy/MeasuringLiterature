# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:44:59 2018

@author: M Manguy
"""

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
import matplotlib as mpl
from random import sample
import re
"""
Macbeth Baritone  M-L   General of King Duncan's army
Lady Macbeth  Soprano F-H   Wife of Macbeth
Banco Bass  M-VL  General of King Duncan's army
Macduff Tenor M-M   Scottish nobleman, Lord of Fiff
Lady-in-waiting Mezzosoprano  F-M   Attending on Lady Macbeth
Malcolm Tenor M-M   King Duncan's son
Doctor  Bass  M-VL  
Servant of Macbeth  Bass  M-VL  
Herald  Bass  M-VL  
Assassin  Bass  M-VL  
Duncano       King of Scotland
Fleanzio
"""
file = open("MacBeth_o.txt", "r",encoding='utf8')
lines=file.readlines()
character=['MACBETH',
           'LADY MACBETH',
           'BANCO',
           'MACDUFF',
           'MALCOLM',
           'STREGHE',
           'SICARIO',
           'MESSAGGERI',
           'DAMA',
           'MEDICO',
           'ARALDO',
           'FLEANZIO',
           'SERVO',
           'CORO']
EdgesValues=np.zeros((len(character),len(character)))
for i,data in enumerate(lines):
    ligne=data.split('.')
    if ligne[0] in character:
        j=0
        number=0
        if data.strip('\n') == 'Top':
            break
        while lines[i+j] !='\n':
            j+=1
            number += len(lines[i+j].split(' '))
        #print(number)
        source=ligne[0]
        destinations=ligne[1].split("]")[0].strip("[").split(",")
        for dest in destinations:
            if dest in character:
              EdgesValues[character.index(source),character.index(dest)]+=number
"""
print(EdgesValues)
A=np.array(EdgesValues)
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
plt.show()
"""
A=np.matrix(EdgesValues)
A=np.delete(A, 0, 0)
A=np.delete(A, 0, 1)
print(A)

G=nx.from_numpy_matrix(A,create_using = nx.MultiDiGraph())
##Edge calculation
colors=[A[x,y] for x,y in G.edges()]
##label design
labels={}
print(character)
character.pop(0)
print(character)
for i,char in enumerate(character):
    labels[i]=char
fig = plt.figure()
nx.draw(G,pos=nx.nx_agraph.graphviz_layout(G),
        labels=labels,with_labels=True,arrows=False,
        edge_color=colors,edge_cmap=plt.cm.YlOrRd,width=2,
        node_color='cadetblue',font_size=12,
        font_color='olivedrab',font_weight='bold')
fig.patch.set_facecolor("#353432")
mpl.rcParams['savefig.facecolor'] = "#353432"
plt.savefig('MB_O_cs.png')
plt.show()
