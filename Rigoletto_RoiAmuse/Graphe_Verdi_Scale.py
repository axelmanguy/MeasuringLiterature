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
file = open("Giuseppe Verdi - Rigoletto (Italian–English)_modified.txt", "r",encoding='utf8')
lines=file.readlines()
actes=[lines[:405],lines[404:1079],lines[1083:1484],lines[1484:2107],lines[2107:]]
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
for k,act in enumerate(actes):
  lines=act
  EdgesValues=np.zeros((len(character),len(character)))
  for i,data in enumerate(lines):
      line=data.split('[')
      j=0
      number=0
      if data.strip('\n') == 'FINE':
          break
      while lines[i+j] !='\n':
          j+=1
          print(lines[i])
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
  pp.pprint(EdgesValues)
  print('----------------------')
  print(np.min(EdgesValues))
  print(np.max(EdgesValues))
  print('----------------------')
  A=np.matrix(EdgesValues)
  G=nx.from_numpy_matrix(A,create_using = nx.MultiDiGraph())
  #Edge calculation
  colors=[EdgesValues[x][y] for x,y in G.edges()]
  #label design
  labels={}
  pos = {0: (-14.417, -0.24801),
         1: (-0.21228, 40),
         2: (-76.96, 36.377),
         3: (-58.54, 72.957),
         4: (-22.74, 94.212),
         5: (-95.982, -15.488),
         6: (45.91, 73.076),
         7: (4.8583, -55.399),
         8: (45.054, -56.784),
         9: (-69.559, -73.872),
         10: (117.63, -83.038),
         11: (56.893, 14.381),
         12: (68.063, -25.612)}
  for i,char in enumerate(character):
      labels[i]=char
  fig = plt.figure()
  nx.draw(G,pos=nx.nx_agraph.graphviz_layout(G),
  		labels=labels,with_labels=True,arrows=False,
         edge_color=colors,edge_cmap=plt.cm.YlOrRd,width=2,
  		node_color='cadetblue',font_size=12,
         font_color='darkolivegreen',font_weight='bold')
  fig.patch.set_facecolor("#353432")
  mpl.rcParams['savefig.facecolor'] = "#353432"
  plt.savefig('Acte_Rigolleto_'+str(k)+'.png')
  plt.show()
