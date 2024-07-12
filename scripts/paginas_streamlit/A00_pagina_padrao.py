def barra_lateral_padrao(data,st):

    #HEADER

    #st.sidebar.image('./imagens/logo.png',width=120)
    st.sidebar.markdown('# FOME ZERO')
    st.sidebar.markdown('## Nosso negócio é matar a sua fome.')
    st.sidebar.markdown("""---""")

    #FILTROS

    opcoes=['SIM', 'NÃO']
    Has_Table_booking=st.sidebar.multiselect('Faz reserva',opcoes,default=opcoes)

    opcoes=['SIM', 'NÃO']
    Is_delivering_now=st.sidebar.multiselect('Faz entregas',opcoes,default=opcoes)

    opcoes=['SIM', 'NÃO']
    Has_Online_delivery=st.sidebar.multiselect('Aceita pedidos online',opcoes,default=opcoes)


    opcoes=['expencive', 'gourmet', 'normal', 'cheap']
    Price_range=st.sidebar.multiselect('Faixas de preço',opcoes,default=opcoes)

    opcoes=['Philippines', 'Brazil', 'Australia', 'United States of America',
        'Canada', 'Singapure', 'United Arab Emirates', 'India',
        'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
        'Sri Lanka', 'Turkey']
    Country_name=st.sidebar.multiselect('País',opcoes,default=opcoes)

    st.sidebar.markdown("""---""")

    #APLICAR FILTROS
    filtro_linhas=((data['Has_Table_booking'].isin(Has_Table_booking))&
                (data['Is_delivering_now'].isin(Is_delivering_now))&
                (data['Has_Online_delivery'].isin(Has_Online_delivery))&
                (data['Price_range'].isin(Price_range))&
                (data['Country_name'].isin(Country_name))
                )
    data=data.loc[filtro_linhas,:]
    return data