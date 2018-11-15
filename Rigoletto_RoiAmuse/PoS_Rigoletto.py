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
tags={'ABR':'abbreviation',
'ADJ':'adjective',
'ADV':'adverb',
'CON':'conjunction',
'DET:def':'definite article',
'DET:indef':'indefinite article',
'FW ':'foreign word',
'INT':'interjection',
'LS ':'list symbol',
'NOM':'noun',
'NPR':'name',
'NUM':'numeral',
'PON':'punctuation',
'PRE':'preposition',
'PRE:det':'preposition+article',
'PRO':'pronoun',
'PRO:demo':'demonstrative pronoun',
'PRO:indef':'indefinite pronoun',
'PRO:inter':'interrogative pronoun',
'PRO:pers':'personal pronoun',
'PRO:poss':'possessive pronoun',
'PRO:refl':'reflexive pronoun',
'PRO:rela':'relative pronoun',
'SENT':'sentence marker',
'SYM':'symbol',
'VER:cimp':'verb conjunctive imperfect',
'VER:cond':'verb conditional',
'VER:cpre':'verb conjunctive present',
'VER:futu':'verb future tense',
'VER:geru':'verb gerund',
'VER:impe':'verb imperative',
'VER:impf':'verb imperfect',
'VER:infi':'verb infinitive',
'VER:pper':'verb participle perfect',
'VER:ppre':'verb participle present',
'VER:pres':'verb present',
'VER:refl:infi':'verb reflexive infinitive',
'VER:remo':'verb simple past'}
#DUCA, RIGOLETTO[BORSA, CEPRANO, MARULLO, CORO]
tagger = treetaggerwrapper.TreeTagger(TAGLANG='it')
file = open("Giuseppe Verdi - Rigoletto (Italian–English)_modified.txt", "r",encoding='utf8')
lines=file.readlines()
character=['DUCA','RIGOLETTO','GILDA','SPARAFUCILE','MADDALENA',
            'GIOVANNA','MONTERONE','MARULLO','BORSA','CONTESSA',
            'PAGGIO','CORO','CEPRANO']
charLines={key:[] for key in character}
charLines_dest={key:{key2:[] for key2 in character} for key in character}

charSentences={key:[""] for key in character}
charSentences_dest={key:{key2:[""] for key2 in character} for key in character}

charTags={key:{key2:0 for key2 in tags.keys()} for key in character}
charTags_dest={key:{key2:{key3:0 for key3 in tags} for key2 in character} for key in character}

EdgesValues=np.zeros((len(character),len(character)))
for i,data in enumerate(lines):
    if data.strip('\n') == 'FINE':
            break
    ligne=data.split('[')
    for source in ligne[0].split(","):
        if source in character:
            j=0
            text=[]
            while lines[i+j] !='\n':
                j+=1
                if len(lines[i+j]) > 1:
                    text.append(lines[i+j].strip('\n'))
            for l in text:
                if l[0] != '/':
                    charLines[source].append(l)
            if len(ligne)>1: #if there is destinations specified /ecc./
                destinations=ligne[1].split("]")[0].strip("[").split(",")
                for dest in destinations:
                    if dest in character:
                        for l in text:
                            if l[0] != '/':
                                charLines_dest[source][dest].append(l)
                        EdgesValues[character.index(source),character.index(dest)]+=1
#sentence constitution
for key,value in charLines.items():
    for i,stc in enumerate(value):
        #if the sentence is not complete
        if not stc.strip('\n')[-1] in ['.','?','!','/']:
            j=0
            sentence=stc.strip('\n')
            print(value)
            while not value[i+j].strip('\n')[-1] in ['.','?','!','/']:
                print(value[i+j].strip('\n')[-5:-1])
                j+=1
                sentence+=" "+value[i+j].strip('\n')
            if sentence not in charSentences[key][-1]:
                charSentences[key].append(sentence)
                print(sentence)
        elif stc.strip('\n')[-1] in ['.','?','!','/'] and stc.strip('\n') not in charSentences[key][-1]:
            charSentences[key].append(stc.strip('\n'))

#sentence constitution with destination
for key2,value2 in charLines_dest.items():
    for key,value in value2.items():
        for i,stc in enumerate(value):
            #if the sentence is not complete
            if not stc.strip('\n')[-1] in ['.','?','!','/']:
                j=0
                sentence=stc.strip('\n')
                print(value)
                while not value[i+j].strip('\n')[-1] in ['.','?','!','/']:
                    print(value[i+j].strip('\n'))
                    print(value[i+j].strip('\n')[-1])
                    j+=1
                    sentence+=" "+value[i+j].strip('\n')
                if sentence not in charSentences_dest[key2][key][-1]:
                    charSentences_dest[key2][key].append(sentence)
            elif stc.strip('\n')[-1] in ['.','?','!'] and stc.strip('\n') not in charSentences_dest[key2][key][-1]:
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
#Edges value creation
EdgesValues=np.zeros((len(character),len(character)))
for key2,value2 in charTags_dest.items():
    for key,value in value2.items():
        EdgesValues[character.index(key2),character.index(key)]=max(0,100*(value['VER:impf']/(np.sum(list(value.values())))))
A=np.matrix(EdgesValues)
print(A)
G=nx.from_numpy_matrix(A,create_using = nx.DiGraph())
colors=[EdgesValues[x][y] for x,y in G.edges()]
##label design
labels={}
for i,char in enumerate(character):
    labels[i]=char
fig = plt.figure()
nx.draw(G,pos=nx.nx_agraph.graphviz_layout(G),
        labels=labels,with_labels=True,arrows=False,
       edge_color=colors,edge_cmap=plt.cm.Greens,width=2,
        node_color="#2790B0",font_size=12,
       font_color='darkolivegreen',font_weight='bold')
fig.patch.set_facecolor("#353432")
mpl.rcParams['savefig.facecolor'] = "#353432"
plt.savefig('IMPE_Verdi.png')
plt.show()