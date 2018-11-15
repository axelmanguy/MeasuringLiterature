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
CONTE DI ALMAVIVA (baritone)
LA CONTESSA DI ALMAVIVA (soprano)
SUSANNA (soprano)
FIGARO (bass)
CHERUBINO (soprano or mezzo-soprano)
MARCELLINA (mezzo-soprano)
BARTOLO (bass)
BASILIO (tenor)
DON CURZIO (tenor)
BARBARINA (soprano)
ANTONIO (bass)
CHORUS
"""
file = open("Figaro_M.txt", "r",encoding='utf8')
lines=file.readlines()
character=['CONTE',
           'CONTESSA',
           'SUSANNA',
           'FIGARO',
           'CHERUBINO',
           'MARCELLINA',
           'BARTOLO',
           'BASILIO',
           'DON CURZIO',
           'BARBARINA',
           'ANTONIO',
           'CORO']
EdgesValues=np.zeros((len(character),len(character)))
for i,data in enumerate(lines):
    ligne=data.split('.')
    #print(ligne)
    if ligne[0] in character:
        print(ligne[0])
        j=0
        number=0
        if data.strip('\n') == 'Top':
            break
        while lines[i+j] !='\n':
            j+=1
            number += len(lines[i+j].split(' '))
            print(lines[i+j])
        source=ligne[0]
        destinations=ligne[1].split("]")[0].strip("[").split(",")
        for dest in destinations:
            print(dest)
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
A=np.delete(A, 1, 0)
A=np.delete(A, 1, 1)
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
plt.savefig('Figaro_M_cs_compte.png')
plt.show()
