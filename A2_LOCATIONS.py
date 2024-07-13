#streamlit run visao_negocio.py
#========================================
#LOAD DATA
from scripts.manipular_dados.A00_leitura_dados import ler_dados
dados=ler_dados()

#========================================
#IMPORT LIBS
import plotly.express as px
import streamlit as st

from scripts.paginas_streamlit.A00_pagina_padrao import barra_lateral_padrao

#========================================
#layout 
#========================================
st.set_page_config(
    page_title='Zero Hunger',
    page_icon="🍽️",
    layout='wide')
#========================================
#SIDE BAR
dados=barra_lateral_padrao(dados,st)
#========================================
#HEADER
st.header('GEOGRAPHIC VIEW')
#========================================
#FUNCTIONS TO DATA
#========================================

#========================================
#SECTIONS
v_civ_contryty,v_city,v_map=st.tabs(['CONTRIES','CITIES','MAP'])
#========================================
#GENERAL NUMBERS
with st.container(): 
    st.markdown("##### GENERAL NUMBERS")
    col_1,col_2,col_3,col_4,col_5=st.columns(5)
    with col_1:
        st.metric(label='Registered cities',value=0)
    with col_2:
        st.metric(label='Registered restaurants',value=0)
    with col_3:
        st.metric(label='Ratings',value=0)
    with col_4:
        st.metric(label='Cuisines',value=0)
    with col_5:
        st.metric(label='Average Cost for two',value=0)
with st.container(): 
    st.markdown("##### MAIN NUMBERS FOR COUNTRIES")
    

#========================================