#streamlit run visao_negocio.py
#========================================
#preparar dados
from scripts.manipular_dados.A00_leitura_dados import ler_dados
dados=ler_dados()

#========================================
#importar bibliotecas
from datetime import datetime
import plotly.express as px
import streamlit as st

from scripts.paginas_streamlit.A00_pagina_padrao import barra_lateral_padrao

#========================================
#layout 
#========================================
st.set_page_config(
    page_title='FOME ZERO',
    page_icon="🍽️",
    layout='wide'
)

#SIDE BAR
dados=barra_lateral_padrao(dados,st)

#HEADER
st.header('VISÃO GERAL')

#========================================
#LAYOUT
#========================================


#========================================


with st.container(): 

    col_restaurantes,col_pais,col_cidade,col_avaliacao,col_culinaria=st.columns(5)

    with col_restaurantes:
        st.metric(label='RESTAURANTES ÚNICOS',value=0)
    with col_pais:
        st.metric(label='PAÍSES CADASTRADOS',value=0)
    with col_cidade:
        st.metric(label='CIDADES ATENDIDAS',value=0)
    with col_avaliacao:
        st.metric(label='AVALIAÇÕES RECEBIDAS',value=0)
    with col_culinaria:
        st.metric(label='CULINÁRIAS DISPONÍVEIS',value=0)

with st.container(): 
    pass

#========================================