# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:22:19 2024

@author: mrijneveld
"""

import streamlit as st

st.title('Test-pagina voor widgets')
'Dit is een pagina om de verschillende widgets te testen'

var1=st.slider('eerste getal:',min_value=0.0, max_value=100.0, step=1.0)
var2=st.number_input('tweede getal?',min_value=0.0, max_value=10, step=0.5)
operator=st.radio('kies een actie',['plus','min','keer','gedeeld door'])
if operator=='plus':
    answer = var1 + var2
    
elif operator=='min':
    answer = var1 - var2
    
elif operator=='keer':
    answer = var1 * var2

elif operator=='gedeeld door':
    answer = var1 / var2

'het antwoord op de actie met de twee getallen is:'
st.text(answer)

''
but1=st.button('click me!')
if but1 == True:
    st.balloons()

