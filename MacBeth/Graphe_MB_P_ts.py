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
    DUNCAN, King of Scotland.
    MALCOLM, his Son.
    DONALBAIN, his Son.
    MACBETH, General in the King's Army.
    BANQUO, General in the King's Army.
    MACDUFF, Nobleman of Scotland.
    LENNOX, Nobleman of Scotland.
    ROSS, Nobleman of Scotland.
    MENTEITH, Nobleman of Scotland.
    ANGUS, Nobleman of Scotland.
    CAITHNESS, Nobleman of Scotland.
    FLEANCE, Son to Banquo.
    SIWARD, Earl of Northumberland, General of the English Forces.
    YOUNG SIWARD, his Son.
    SEYTON, an Officer attending on Macbeth.
    BOY, Son to Macduff.
    An English Doctor. A Scottish Doctor. A Soldier. A Porter. An Old Man.

    LADY MACBETH.
    LADY MACDUFF.
    Gentlewoman attending on Lady Macbeth.
    HECATE,and three Witches.

    Lords, Gentlemen, Officers, Soldiers, Murderers, Attendants, and Messengers.

    The Ghost of Banquo and several other Apparitions. 
"""
file = open("MacBeth_p.txt", "r",encoding='utf8')
lines=file.readlines()
actes=[lines[:977],lines[978:1813],lines[1814:2787],lines[2788:3879],lines[3880:]]
character=['DUNCAN',
           'MALCOLM',
           'DONALBAIN',
           'MACBETH',
           'LADY MACBETH',
           'BANQUO',
           'MACDUFF',
           'LADY MACDUFF',
           'SON',
           'LENNOX',
           'ROSS',
           'MENTEITH',
           'ANGUS',
           'CAITHNESS',
           'FLEANCE',
           'SIWARD',
           'SEYTON',
           'DOCTOR',
           'OLD MAN',
           'SERVANT',
           'GENTLEWOMAN',
           'HECATE',
           'FIRST WITCH',
           'SECOND WITCH',
           'THIRD WITCH',
           'FIRST MURDERER',
           'SECOND MURDERER',
           'THIRD MURDERER']
for k,act in enumerate(actes):
  lines=act
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
  plt.savefig('MBP_Acte_'+str(k)+'.png')
  plt.show()