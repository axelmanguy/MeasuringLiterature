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
##################
# MAC BETH PLAY  #
##################
file = open("MacBeth_p.txt", "r",encoding='utf8')
lines=file.readlines()
character=['MACBETH',
           'MALCOLM',
           'DONALBAIN',
           'DUNCAN',
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
EdgesValues=np.zeros((len(character),len(character)))
EdgesNum=np.zeros((len(character),len(character)))
for i,data in enumerate(lines):
    ligne=data.split('.')
    #print(ligne)
    if ligne[0] in character:
        print(ligne[0])
        j=2
        number=0
        if data.strip('\n') == 'Top':
            break
        while lines[i+j] !='\n':
            j+=1
            number += len(lines[i+j].split(' '))
        print(number)
        source=ligne[0]
        destinations=ligne[1].split("]")[0].strip("[").split(",")
        for dest in destinations:
            print(dest)
            if dest in character:
              EdgesNum[character.index(source),character.index(dest)]+=1
              EdgesValues[character.index(source),character.index(dest)]+=number
print(EdgesValues)
A=np.array(EdgesValues)
names,values,values2=[],[],[]
for i,char in enumerate(character):
    names.append(char)
    values.append(100*(np.sum(EdgesValues[i])/(np.sum(np.sum(EdgesValues)))))
    values2.append(100*(np.sum(EdgesNum[i])/(np.sum(np.sum(EdgesNum)))))
values=np.array(values)
values2=np.array(values2)
plt.scatter(values,values2, label='macbeth_play')

##################
# MAC BETH OPERA #
##################

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
EdgesNum=np.zeros((len(character),len(character)))
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
        print(number)
        source=ligne[0]
        destinations=ligne[1].split("]")[0].strip("[").split(",")
        for dest in destinations:
            print(dest)
            if dest in character:
              EdgesNum[character.index(source),character.index(dest)]+=1
              EdgesValues[character.index(source),character.index(dest)]+=number
print(EdgesValues)
A=np.array(EdgesValues)
names,values,values2=[],[],[]
for i,char in enumerate(character):
    names.append(char)
    values.append(100*(np.sum(EdgesValues[i])/(np.sum(np.sum(EdgesValues)))))
    values2.append(100*(np.sum(EdgesNum[i])/(np.sum(np.sum(EdgesNum)))))
values=np.array(values)
values2=np.array(values2)
plt.scatter(values,values2, label='macbeth_opera')

###############
# FIGARO PLAY #
###############

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
EdgesNum=np.zeros((len(character),len(character)))
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
        print(number)
        source=ligne[0]
        destinations=ligne[1].split("]")[0].strip("[").split(",")
        for dest in destinations:
            print(dest)
            if dest in character:
              EdgesNum[character.index(source),character.index(dest)]+=1
              EdgesValues[character.index(source),character.index(dest)]+=number
print(EdgesValues)
A=np.array(EdgesValues)
names,values,values2=[],[],[]
for i,char in enumerate(character):
    names.append(char)
    values.append(100*(np.sum(EdgesValues[i])/(np.sum(np.sum(EdgesValues)))))
    values2.append(100*(np.sum(EdgesNum[i])/(np.sum(np.sum(EdgesNum)))))
values=np.array(values)
values2=np.array(values2)
plt.scatter(values,values2, label='figaro_opera')

###############
# FIGARO PLAY #
###############
file = open("Figaro_B.txt", "r",encoding='utf8')
lines=file.readlines()
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
EdgesValues=np.zeros((len(character),len(character)))
EdgesNum=np.zeros((len(character),len(character)))
for i,data in enumerate(lines):
    ligne=data.split('.')
    #print(ligne)
    if ligne[0] in character:
        print(ligne[0])
        j=2
        number=0
        if data.strip('\n') == 'Top':
            break
        while lines[i+j] !='\n':
            j+=1
            number += len(lines[i+j].split(' '))
        print(number)
        source=ligne[0]
        destinations=ligne[1].split("]")[0].strip("[").split(",")
        for dest in destinations:
            print(dest)
            if dest in character:
              EdgesNum[character.index(source),character.index(dest)]+=1
              EdgesValues[character.index(source),character.index(dest)]+=number
print(EdgesValues)
A=np.array(EdgesValues)
names,values,values2=[],[],[]
for i,char in enumerate(character):
    names.append(char)
    values.append(100*(np.sum(EdgesValues[i])/(np.sum(np.sum(EdgesValues)))))
    values2.append(100*(np.sum(EdgesNum[i])/(np.sum(np.sum(EdgesNum)))))
values=np.array(values)
values2=np.array(values2)
plt.scatter(values,values2, label='figaro_play')


##################
# Le Roi s'amuse #
##################
file = open("Giuseppe Verdi - Rigoletto (Italian–English)_modified.txt", "r",encoding='utf8')
lines=file.readlines()
EdgesNum=np.zeros((len(character),len(character)))
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
EdgesValues=np.zeros((len(character),len(character)))
for i,data in enumerate(lines):
    line=data.split('[')
    j=0
    number=0
    if data.strip('\n') == 'FINE':
        break
    while lines[i+j] !='\n':
        j+=1
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
                    EdgesNum[character.index(source),character.index(dest)]+=1
                    EdgesValues[character.index(source),character.index(dest)]+=number
print(EdgesValues)
A=np.array(EdgesValues)
names,values,values2=[],[],[]
for i,char in enumerate(character):
    names.append(char)
    values.append(100*(np.sum(EdgesValues[i])/(np.sum(np.sum(EdgesValues)))))
    values2.append(100*(np.sum(EdgesNum[i])/(np.sum(np.sum(EdgesNum)))))
values=np.array(values)
values2=np.array(values2)
plt.scatter(values,values2, label='Rigoletto')

##################
# Le roi s'amuse #
##################
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
EdgesNum=np.zeros((len(character),len(character)))
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
              EdgesNum[character.index(source),character.index(dest)]+=1
              EdgesValues[character.index(source),character.index(dest)]+=number
print(EdgesValues)
A=np.array(EdgesValues)
names,values,values2=[],[],[]
for i,char in enumerate(character):
    names.append(char)
    values.append(100*(np.sum(EdgesValues[i])/(np.sum(np.sum(EdgesValues)))))
    values2.append(100*(np.sum(EdgesNum[i])/(np.sum(np.sum(EdgesNum)))))
values=np.array(values)
values2=np.array(values2)
plt.scatter(values,values2, label="Le roi s'amuse")

plt.legend()
plt.show()