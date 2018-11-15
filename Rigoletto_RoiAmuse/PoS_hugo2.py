# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 08:54:47 2018

@author: M Manguy
"""
from io import StringIO
import pandas as pd
import treetaggerwrapper
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
from random import sample
import re
tags={'ABR':'abreviation',
'ADJ':'adjective',
'ADV':'adverb',
'DET:ART':'article',
'DET:POS':'possessive pronoun (ma, ta, ...)',
'INT':'interjection',
'KON':'conjunction',
'NAM':'proper name',
'NOM':'noun',
'NUM':'numeral',
'PRO':'pronoun',
'PRO:DEM':'demonstrative pronoun',
'PRO:IND':'indefinite pronoun',
'PRO:PER':'personal pronoun',
'PRO:POS':'possessive pronoun (mien, tien, ...)',
'PRO:REL':'relative pronoun',
'PRP':'preposition',
'PRP:det':'preposition plus article (au,du,aux,des)',
'PUN':'punctuation',
'PUN:cit':'punctuation citation',
'SENT':'sentence tag',
'SYM':'symbol',
'VER:cond':'verb conditional',
'VER:futu':'verb futur',
'VER:impe':'verb imperative',
'VER:impf':'verb imperfect',
'VER:infi':'verb infinitive',
'VER:pper':'verb past participle',
'VER:ppre':'verb present participle',
'VER:pres':'verb present',
'VER:simp':'verb simple past',
'VER:subi':'verb subjunctive imperfect',
'VER:subp':'verb subjunctive present'}
tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')
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

charLines={key:[] for key in character}
charLines_dest={key:{key2:[] for key2 in character} for key in character}

charSentences={key:[""] for key in character}
charSentences_dest={key:{key2:[""] for key2 in character} for key in character}

charTags={key:{key2:0 for key2 in tags.keys()} for key in character}
charTags_dest={key:{key2:{key3:0 for key3 in tags} for key2 in character} for key in character}

EdgesValues=np.zeros((len(character),len(character)))
for i,data in enumerate(lines):
    ligne=data.split('.')
    if ligne[0] in character:
        j=0
        text=[]
        if data.strip('\n') == 'FIN':
            break
        while lines[i+j] !='\n':
            j+=1
            if len(lines[i+j]) > 1:
                text.append(lines[i+j].strip('\n'))
        source=ligne[0]
        for l in text:
            if l[0] != '_' and l[-1] not in ['_','_.'] :
                charLines[source].append(l)
        destinations=ligne[1].split("]")[0].strip("[").split(",")
        for dest in destinations:
            if dest in character:
                EdgesValues[character.index(source),character.index(dest)]+=1
                for l in text:
                    if l[0] != '_' and l[-1] not in ['_','_.']:
                        charLines_dest[source][dest].append(l)

#sentence constitution
for key,value in charLines.items():
    for i,stc in enumerate(value):
        #if the sentence is not complete
        if not stc.strip('\n')[-1] in ['.','?','!']:
            j=0
            sentence=stc.strip('\n')
            while not value[i+j].strip('\n')[-1] in ['.','?','!']:
                j+=1
                sentence+=" "+value[i+j].strip('\n')
            if sentence.lower() not in charSentences[key][-1]:
                charSentences[key].append(sentence.lower())
        elif stc.strip('\n')[-1] in ['.','?','!'] and stc.strip('\n').lower() not in charSentences[key][-1]:
            charSentences[key].append(stc.strip('\n'))

#sentence constitution with destination
for key2,value2 in charLines_dest.items():
    for key,value in value2.items():
        for i,stc in enumerate(value):
            #if the sentence is not complete
            if not stc.strip('\n')[-1] in ['.','?','!']:
                j=0
                sentence=stc.strip('\n')
                #print(stc.strip('\n'))
                #print(stc.strip('\n')[-1])
                while not value[i+j].strip('\n')[-1] in ['.','?','!']:
                    j+=1
                    sentence+=" "+value[i+j].strip('\n')
                if sentence.lower() not in charSentences_dest[key2][key][-1]:
                    charSentences_dest[key2][key].append(sentence.lower())
            elif stc.strip('\n')[-1] in ['.','?','!'] and stc.strip('\n').lower() not in charSentences_dest[key2][key][-1]:
                charSentences_dest[key2][key].append(stc.strip('\n'))

#PoS tagging
for key,value in charSentences.items():
    for i,stc in enumerate(value):
        tags = tagger.tag_text(stc)
        pos=[i.pos for i in treetaggerwrapper.make_tags(tags)]
        unique,num=np.unique(pos, return_counts=True)
        for k,tag in enumerate(unique):
            charTags[key][tag]+=num[k]

#PoS tagging with dest
for key2,value2 in charSentences_dest.items():
    for key,value in value2.items():
        for i,stc in enumerate(value):
            tags = tagger.tag_text(stc)
            pos=[i.pos for i in treetaggerwrapper.make_tags(tags)]
            unique,num=np.unique(pos, return_counts=True)
            for k,tag in enumerate(unique):
                charTags_dest[key2][key][tag]+=num[k]

"""
for char in character:
    names = list(charTags[char].keys())
    values = list(charTags[char].values())
    plt.bar(names, values)
    plt.xticks(rotation=90)
    plt.yticks(rotation=90)
    plt.title(char)
    plt.show()
"""
"""
[[0.         0.         0.10141988 0.         0.         0. 0.          0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.20703934 0.         0.         0.         0.  0.22779043 0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.13404826 0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.68493151 0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.10559662 1.25       0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.  0.         0.         0.         0.         0.         0.        ]]

"""
#Edges value creation
EdgesValues=np.zeros((len(character),len(character)))
for key2,value2 in charTags_dest.items():
    for key,value in value2.items():
        EdgesValues[character.index(key2),character.index(key)]=max(0,100*(value['VER:impe']/(np.sum(list(value.values())))))
A=np.matrix(EdgesValues)
A=A[:7,:7]
G=nx.from_numpy_matrix(A,create_using = nx.MultiDiGraph())
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
colors=[max(0,EdgesValues[x][y]) for x,y in G.edges()]
print(colors)
##label design
labels={}
for i,char in enumerate(character):
    if i<7:
        labels[i]=char
fig = plt.figure()
print(labels)
nx.draw(G,
        labels=labels,with_labels=True,arrows=False,
       edge_color=colors,edge_cmap=plt.cm.Greens,width=2,
        node_color="#2790B0",font_size=12,
       font_color='darkolivegreen',font_weight='bold')
fig.patch.set_facecolor("#353432")
mpl.rcParams['savefig.facecolor'] = "#353432"
plt.savefig('IMP_hugo.png')
plt.show()