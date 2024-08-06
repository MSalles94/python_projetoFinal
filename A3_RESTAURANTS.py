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
st.header('RESTAURANTS VIEW')
#========================================
#FUNCTIONS TO DATA
#========================================

from scripts.paginas_streamlit import A03_calculos_pg_restaurantes as respostas

#========================================
#SECTIONS
v_restaurants,v_cuisines=st.tabs(['RESTAURANTS','CUISINES'])
#========================================
with v_restaurants: 

    with st.container():
        col_restaurant,col_price,col_votes,col_rate=st.columns(4)

        with col_restaurant:
            st.metric(label='Registered restaurants',value=respostas.registred_restaurants(dados))
        
        with col_price:
            st.metric(label='Average meal price',value=respostas.avg_price_forTwo(dados))

        with col_votes:
            st.metric(label='Votes',value=respostas.num_votes(dados))
        
        with col_rate:
            st.metric(label='Rate',value=respostas.total_rate(dados))
    
    with st.container():
        col_booking,col_delivery,col_online=st.columns(3)
        
        with col_booking:
            st.metric(label='Accept booking',value=respostas.accept_booking(dados))

        with col_delivery:
            st.metric(label='Is delivering',value=respostas.accept_delivery(dados))

        with col_online:
            st.metric(label='Accept online delivery',value=respostas.accept_online_delivery(dados))

    with st.container():
        st.markdown('---')
        st.markdown('## Brazilian cuisine')

        worst_brazilien,top_brazilien_brazil=st.columns(2)

        with worst_brazilien:
            st.markdown('#### Worst rated Brazilian cuisine')
            st.dataframe(respostas.botton_brasilien_restaurants(dados))
        with top_brazilien_brazil:
            st.markdown('#### Top rated Brazilian cuisine in Brazil')
            st.dataframe(respostas.top_brasilien_restaurants(dados))
    with st.container():
        st.markdown('---')
        st.markdown('#### Top most Expensive Restaurants')
        st.plotly_chart(respostas.top_avg_price(dados),use_container_width=True)
     

    with st.container():
        st.markdown('---')
        v1,v2,v3=st.columns(3)
        
        with v1:
            st.markdown('#### Average cost for booking restaurants')
            st.plotly_chart(respostas.avg_cost_booking(dados),use_container_width=True)
        with v2:
            st.markdown('#### Average Votes per online restaurants')
            st.plotly_chart(respostas.avg_votes_online(dados),use_container_width=True)
        with v3:
            st.markdown('#### Average Cost - BBQ versus Japanese ')
            st.plotly_chart(respostas.cost_BBQ_verus_japa(dados),use_container_width=True)
           
with v_cuisines:
    with st.container():
        st.markdown('### MAIN STATISTICS')
        v1,v2,v3=st.columns(3)

        with v1: 
            st.markdown('#### TOP expensive cuisines')
            st.plotly_chart( respostas.cuisine_value_for_two(dados),use_container_width=True)
        with v2: 
            st.markdown('#### TOP rated cuisines')
            st.plotly_chart( respostas.cuisine_avg_rate(dados),use_container_width=True)
        with v3:
            st.markdown('#### Cuisines with online delivering')
            st.plotly_chart( respostas.cuisine_online_delivers(dados),use_container_width=True)

    with st.container():
        st.markdown('### TOP RATE - SELECTED CUISINES')

        opcoes=['Arabian','American','Italian','Japanese','Home-made']
        cuisines_filter=st.multiselect('Cuisines filter',opcoes,default=opcoes)

        v1,v2=st.columns(2)

        with v1:
            st.markdown('#### Worst rated restaurants')
            df=respostas.top_rating_cuisine(dados,filter_c=cuisines_filter,worst_rating=True)
            st.dataframe(df,use_container_width=True)
        with v2:
            st.markdown('#### Best rated restaurants')
            df=respostas.top_rating_cuisine(dados,filter_c=cuisines_filter,worst_rating=False)
            st.dataframe(df,use_container_width=True)

         
#========================================