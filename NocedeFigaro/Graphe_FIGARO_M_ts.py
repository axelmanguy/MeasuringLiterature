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
#actes selection
#actes=[lines[:1242],lines[1243:2450],lines[2450:3351],lines[3351:4411],lines[4411:]]
actes=[lines[:1087],lines[1088:2680],lines[2681:3776],lines[3777:]]
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
for k,act in enumerate(actes):
  lines=act
  EdgesValues=np.zeros((len(character),len(character)))
  for i,data in enumerate(lines):
      ligne=data.split('.')
      if ligne[0] in character:
          j=0
          number=0
          if data.strip('\n') == 'FINI':
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
  plt.savefig('FIGM_Acte_'+str(k)+'.png')
  plt.show()
