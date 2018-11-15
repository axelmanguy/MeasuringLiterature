# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:44:59 2018

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
LE COMTE ALMAVIVA, grand corrégidor d’Andalousie.

LA COMTESSE, sa femme.

FIGARO, valet de chambre du comte et concierge du château.

SUZANNE, première camériste de la comtesse, et fiancée de Figaro.

MARCELINE, femme de charge.

ANTONIO, jardinier du château, oncle de Suzanne et père de Fanchette.

FANCHETTE, fille d’Antonio.

CHÉRUBIN, premier page du comte.

BARTHOLO, médecin de Séville.

BASILE, maître de clavecin de la comtesse.

DON GUSMAN BRID’OISON, lieutenant du siège.

DOUBLE-MAIN, greffier, secrétaire de don Gusman.

Un huissier audiencier.

GRIPPE-SOLEIL, jeune pastoureau.

Une jeune bergère.

PÉDRILLE, piqueur du comte.
"""
file = open("Figaro_B.txt", "r",encoding='utf8')
lines=file.readlines()
actes=[lines[:1365],lines[1366:3253],lines[3254:4788],lines[4789:5840],lines[5841:]]
character=['FIGARO',
           'LE COMTE',
           'LA COMTESSE',
           'SUZANNE',
           'MARCELINE',
           'ANTONIO',
           'FANCHETTE',
           'BARTHOLO',
           'BASILE',
           'DOUBLE-MAIN',
           'GRIPPE-SOLEIL',
           'PEDRILLE',
           'UN HUISSIER']
for k,act in enumerate(actes):
  lines=act
  EdgesValues=np.zeros((len(character),len(character)))
  for i,data in enumerate(lines):
      ligne=data.split('.')
      if ligne[0] in character:
          j=2
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
