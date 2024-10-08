# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:15:09 2024

@author: mrijneveld
"""

import math as mt
import streamlit as st

def Hangdraden_veld2(L_veld2, a_veld2_stippel_begin=3.5, a_veld2_stippel_eind=1.5, a_veld2_continu_begin1=2.5, a_veld2_continu_begin2=4.0, a_veld2_continu_eind=3.0):
    D2=L_veld2-(a_veld2_continu_begin1+a_veld2_continu_begin2+a_veld2_continu_eind)
    n2=mt.ceil(D2/7.0)
    E2=D2/n2
    #F2=0.5*(D2-(E2*(n2-1)))
    Veld2_hangdraden_stippel=[a_veld2_stippel_begin]
    Veld2_hangdraden_continu=[a_veld2_continu_begin1,a_veld2_continu_begin1+a_veld2_continu_begin2]
    
    for i in range(n2):
        Veld2_hangdraden_continu.append(round((a_veld2_continu_begin1+a_veld2_continu_begin2)+(E2*(i+1)),2))
        Veld2_hangdraden_stippel.append(round((a_veld2_continu_begin1+a_veld2_continu_begin2)+(E2*(i+0.5)),2))

    Veld2_hangdraden_stippel.append(L_veld2-a_veld2_stippel_eind)
    
    return [Veld2_hangdraden_continu,Veld2_hangdraden_stippel]


def Hangdraden_veld3(L_veld3, a_veld3_stippel_begin=3.0, a_veld3_stippel_eind2=4, a_veld3_stippel_eind1=2.5, a_veld3_continu_begin=1.5, a_veld3_continu_eind=3.5 ):
    D3=L_veld3-(a_veld3_stippel_begin+a_veld3_stippel_eind2+a_veld3_stippel_eind1)
    n3=mt.ceil(D3/7.0)
    E3=D3/n3
    #F3=0.5*(D3-(E3*(n3-1)))
    Veld3_hangdraden_stippel=[a_veld3_stippel_begin]
    Veld3_hangdraden_continu=[a_veld3_continu_begin]
    
    for i in range(n3):
        Veld3_hangdraden_stippel.append(round(a_veld3_stippel_begin+E3*(i+1),2))
        Veld3_hangdraden_continu.append(round(a_veld3_stippel_begin+E3*(i+0.5),2))

    Veld3_hangdraden_stippel.append(L_veld3-a_veld3_stippel_eind1)
    Veld3_hangdraden_continu.append(L_veld3-a_veld3_continu_eind)

    return [Veld3_hangdraden_continu, Veld3_hangdraden_stippel]


st.title('testapplicatie voor streamlit - Martin')
st.write('''dit is een tool om de hangdraadverdeling te berekenen voor een OSI over 4 velden.  
         Voor veld 2 en veld 3 (zoals bijlage 12, blad 6 van OVS00024-5.9) kan de indeling voor beide netten berekend worden.
''')
#st.image("Naamloos.jpg", caption="OSI over 4 velden, zonder Y-draden")

L_veld2=st.number_input('Veldlengte veld 2?',min_value=0,value=50)
L_veld3=st.number_input('Veldlengte veld 3?',min_value=0,value=50)


indeling2=Hangdraden_veld2(L_veld2)

onderling2=[[indeling2[0][0]],[indeling2[1][0]]]
for i in range(len(indeling2[0])-1):
    onderling2[0].append(round(indeling2[0][i+1]-indeling2[0][i],2))
    onderling2[1].append(round(indeling2[1][i+1]-indeling2[1][i],2))
    
indeling3=Hangdraden_veld3(L_veld3)

onderling3=[[indeling3[0][0]],[indeling3[1][0]]]
for i in range(len(indeling3[0])-1):
    onderling3[0].append(round(indeling3[0][i+1]-indeling3[0][i],2))
    onderling3[1].append(round(indeling3[1][i+1]-indeling3[1][i],2))

outputtabel2=[['hangdraad', 'afstand (continu)', 'onderling (continu)', 'afstand (gestippeld)', 'onderling (gestippeld)']]
for i in range(len(indeling2[0])):
    outputtabel2.append([i+1, indeling2[0][i], onderling2[0][i], indeling2[1][i], onderling2[1][i]])

outputtabel3=[['hangdraad', 'afstand (continu)', 'onderling (continu)', 'afstand (gestippeld)', 'onderling (gestippeld)']]
for i in range(len(indeling3[0])):
    outputtabel2.append([i+1, indeling3[0][i], onderling3[0][i], indeling3[1][i], onderling3[1][i]])


st.write('')
st.write('Dit is de indeling voor veld 2:')

st.table(outputtabel2)

st.write('')
st.write('En dit is de indeling voor veld 3:')   

st.table(outputtabel3)
