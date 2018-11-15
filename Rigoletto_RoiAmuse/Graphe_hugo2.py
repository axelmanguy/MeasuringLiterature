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
from random import sample
import re
file = open("HUGO.txt", "r",encoding='utf8')
lines=file.readlines()
character=['LE ROI',
           'TRIBOULET',
           'BLANCHE',
           'SALTABADIL',
           'MAGUELONNE',
           'DAME BÉRARDE',
           'MONSIEUR DE SAINT-VALLIER',
           'MAROT',
           'MONSIEUR DE PIENNE',
           'MONSIEUR DE GORDES',
           'MONSIEUR DE PARDAILLAN',
           'MONSIEUR DE BRION',
           'MONSIEUR DE MONTCHENU',
           'MONSIEUR DE MONTMORENCY',
           'MONSIEUR DE COSSÉ',
           'MONSIEUR DE LA TOUR-LANDRY',
           'MADAME DE COSSÉ',
           'LE GENTILHOMME']
EdgesValues=np.zeros((len(character),len(character)))
for i,data in enumerate(lines):
    ligne=data.split('.')
    if ligne[0] in character:
        j=0
        number=0
        if data.strip('\n') == 'FIN':
            break
        while lines[i+j] !='\n':
            j+=1
            number += len(lines[i+j].split(' '))
        print(number)
        source=ligne[0]
        destinations=ligne[1].split("]")[0].strip("[").split(",")
        for dest in destinations:
            if dest in character:
                EdgesValues[character.index(source),character.index(dest)]+=number

print(EdgesValues)
print('----------------------')
print(np.min(EdgesValues))
print(np.max(EdgesValues))
print('----------------------')
A=np.matrix(EdgesValues)
G=nx.from_numpy_matrix(A,create_using = nx.MultiDiGraph())
#positions
pos={0: (13.536, 35.465), 
     1: (-3.0492, 10.549), 
     2: (60.868, 9.1903), 
     3: (27.353, 89.306), 
     4: (76.589, 94.191), 
     5: (80.807, 48.63), 
     6: (-25.367, 101.47), 
     7: (-88.327, -28.448), 
     8: (-12.405, -48.913), 
     9: (-44.319, -3.4472), 
     10: (-48.233, -40.154),
     11: (-6.7033, -85.918), 
     12: (14.038, -38.364), 
     13: (41.7, -116.11), 
     14: (-61.765, 20.946), 
     15: (-71.548, 74.696), 
     16: (114.95, 2.1067), 
     17: (-68.128, -125.2)}

##Edge calculation
colors=[EdgesValues[x][y] for x,y in G.edges()]
##label design
labels={}
for i,char in enumerate(character):
    labels[i]=char
fig = plt.figure()
nx.draw(G,pos,
		labels=labels,with_labels=True,arrows=False,
       edge_color=colors,edge_cmap=plt.cm.YlOrRd,width=2,
		node_color='cadetblue',font_size=12,
       font_color='olivedrab',font_weight='bold')
fig.patch.set_facecolor("#353432")
plt.show()
