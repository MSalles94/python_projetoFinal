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
from scripts.paginas_streamlit import A03_calculos_pg_geografico_ as respostas
#========================================
#SECTIONS
v_civ_contryty,v_city,v_map=st.tabs(['CONTRIES','CITIES','MAP'])
#========================================
#GENERAL NUMBERS
with st.container(): 
    st.markdown("##### GENERAL NUMBERS")
    
    col_1,col_2,col_3,col_4,col_5=st.columns(5)
    with col_1:
        st.metric(label='Registered cities',
                  value=respostas.registred_cities(dados))
    with col_2:
        st.metric(label='Registered restaurants',
                  value=respostas.registred_restaurants(dados))
    with col_3:
        st.metric(label='Ratings',
                  value=respostas.total_votes(dados))
    with col_4:
        st.metric(label='Cuisines',
                  value=respostas.total_cuisines(dados))
    with col_5:
        st.metric(label='Average Cost for two',
                  value=respostas.avg_price_for_two(dados))
with st.container(): 
    st.markdown("##### MAIN NUMBERS FOR COUNTRIES")
    st.dataframe(respostas.generate_geral_df(dados).set_index('Country_name'))

with st.container():
    st.markdown('#### Registred cities per country')
    st.plotly_chart(respostas.grafico_cities(dados), use_container_width=True)

    col_1,col_2=st.columns(2)

with st.container():
    with col_1:
        st.markdown('#### Number of restaurants - if deliver or accept booking')
        st.plotly_chart(respostas.graph_deliver_or_booking(dados), use_container_width=True)

    with col_2:
        st.markdown('#### Average cost for two per price range')
        st.plotly_chart(respostas.graph_priceRange(dados), use_container_width=True)
    
with st.container():

    st.markdown('#### Average cost per price range per country')
    st.plotly_chart(respostas.graph_priceRange_country(dados), use_container_width=True)
    
#========================================