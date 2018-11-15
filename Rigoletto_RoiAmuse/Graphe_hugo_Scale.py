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
import matplotlib as mpl
file = open("HUGO.txt", "r",encoding='utf8')
lines=file.readlines()
actes=[lines[:1242],lines[1243:2450],lines[2450:3351],lines[3351:4411],lines[4411:]]
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
for k,act in enumerate(actes):
  lines=act
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
          #print(number)
          source=ligne[0]
          destinations=ligne[1].split("]")[0].strip("[").split(",")
          for dest in destinations:
              if dest in character:
                  EdgesValues[character.index(source),character.index(dest)]+=number
  print(EdgesValues)
  #print('----------------------')
  #print(np.min(EdgesValues))
  #print(np.max(EdgesValues))
  #print('----------------------')
  A=np.matrix(EdgesValues)
  G=nx.from_numpy_matrix(A,create_using = nx.MultiDiGraph())
  ##Edge calculation
  colors=[EdgesValues[x][y] for x,y in G.edges()]
  ##label design
  labels={}
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
  plt.savefig('Acte_'+str(k)+'.png')
  plt.show()
