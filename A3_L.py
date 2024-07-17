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

def unique_restaurants():
    answer=len(dados['Restaurant_ID'].drop_duplicates())
    return answer
def unique_contries():
    answer=len(dados['Country_name'].drop_duplicates())
    return answer
def unique_cities():
    answer=len(dados['City'].drop_duplicates())
    return answer
def unique_votes():
    answer=len(dados['Votes'].drop_duplicates())
    return answer
def unique_cuisines():
    answer=len(dados['main_Cuisines'].drop_duplicates())
    return answer
def list_of_restaurants(data):
    aux_df=dados.copy()
    aux_df['Restaurant_ID']=aux_df['Restaurant_ID'].astype(str)
    aux_df=aux_df.set_index('Restaurant_ID')
    columns= {  'Restaurant_Name':'Name',
                'Country_name':'Country',
                'City':'City',
                'Votes':'Votes',
                'main_Cuisines':'main_Cuisines'}
    aux_df=aux_df[columns.keys()].rename(columns=columns)
    aux_df=aux_df.drop_duplicates()

    return aux_df

#========================================
with st.container(): 

    col_restaurant,col_contrie,col_city,col_vote,col_cuisines=st.columns(5)

    with col_restaurant:
        st.metric(label='Registered restaurants',value=unique_restaurants())
    with col_contrie:
        st.metric(label='Registered contries',value=unique_contries())
    with col_city:
        st.metric(label='Registered cities',value=unique_cities())
    with col_vote:
        st.metric(label='Ratings',value=unique_votes())
    with col_cuisines:
        st.metric(label='Cuisines',value=unique_cuisines())

with st.container(): 

    st.markdown('## LIST OF RESTAURANTS')
    st.dataframe(list_of_restaurants(dados))

#========================================