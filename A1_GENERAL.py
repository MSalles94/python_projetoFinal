#streamlit run visao_negocio.py
#========================================
#LOAD DATA
from scripts.manipular_dados.A00_leitura_dados import ler_dados
dados=ler_dados()

#========================================
#IMPORT LIBS
#import plotly.express as px
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
st.header('GENERAL VIEW')
#========================================
#FUNCTIONS TO DATA
#========================================

from scripts.paginas_streamlit import A01_calculos_pg_geral_ as resposta

#========================================
with st.container(): 

    col_restaurant,col_contrie,col_city,col_vote,col_cuisines=st.columns(5)

    with col_restaurant:
        st.metric(label='Registered restaurants',value=resposta.unique_restaurants(dados))
    with col_contrie:
        st.metric(label='Registered contries',value=resposta.unique_contries(dados))
    with col_city:
        st.metric(label='Registered cities',value=resposta.unique_cities(dados))
    with col_vote:
        st.metric(label='Ratings',value=resposta.unique_votes(dados))
    with col_cuisines:
        st.metric(label='Cuisines',value=resposta.unique_cuisines(dados))

with st.container(): 

    st.markdown('## LIST OF RESTAURANTS')
    st.dataframe(resposta.list_of_restaurants(dados))

#========================================